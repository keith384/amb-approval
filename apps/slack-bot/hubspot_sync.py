#!/usr/bin/env python3
"""
HubSpot sync (Phase 6) — one-way board → HubSpot. Nothing flows back.

The board is the system of record for approval; HubSpot is the system of record
for the deal. On board events (stage moved, sent to Apple, feedback, approved,
launched) this writes four deal properties + an optional timeline note. Needs a
HubSpot private-app token (deals write) and a per-brand deal mapping
(brands/<brand>/state.json: "hubspot_deal_id"). Dry-run by default — pass --write
to actually patch. The four custom properties must exist (create once with
`ensure-props --write`, the plan's Phase-0 step).

    python hubspot_sync.py map <brand> <deal_id>
    python hubspot_sync.py ensure-props [--write]
    python hubspot_sync.py sync <brand> [--write]
    python hubspot_sync.py note <brand> "<text>" [--link URL] [--write]
"""
from __future__ import annotations
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import request as urlreq, error as urlerr

REPO = Path(__file__).resolve().parent.parent.parent
BRANDS = REPO / "brands"
BASE = "https://api.hubapi.com"

# Property internal names + the stage-label vocabulary (plan).
PROPS = {
    "amb_approval_stage": "AMB approval stage",
    "amb_stage_entered_date": "AMB stage entered date",
    "amb_next_step_owner": "AMB next step owner",
    "amb_last_apple_touch": "AMB last Apple touch date",
}
STAGE_LABEL = {"brand_approval": "Brand Approval", "ux_approval": "UX Approval",
               "experience_review": "Experience Review", "launch": "Launch", "launched": "Launched"}
APPLE_ACTIONS = {"sent_to_apple", "apple_feedback", "approved", "launched"}


def _token() -> str:
    t = os.environ.get("HUBSPOT_PRIVATE_APP_TOKEN", "")
    if not t:
        raise SystemExit("HUBSPOT_PRIVATE_APP_TOKEN not set")
    return t


def _api(method: str, path: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urlreq.Request(f"{BASE}{path}", data=data, method=method,
                         headers={"Authorization": f"Bearer {_token()}", "Content-Type": "application/json"})
    try:
        with urlreq.urlopen(req) as r:
            return json.loads(r.read() or "{}")
    except urlerr.HTTPError as e:
        raise SystemExit(f"HubSpot {method} {path} → {e.code}: {e.read().decode()[:300]}")


def _state(brand: str) -> dict:
    f = BRANDS / brand / "state.json"
    return json.loads(f.read_text()) if f.exists() else {"stage": None, "events": []}


def _save_state(brand: str, st: dict):
    f = BRANDS / brand / "state.json"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(st, indent=2))


def _date_ms(iso: str | None) -> str | None:
    if not iso:
        return None
    try:
        d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return str(int(d.replace(hour=0, minute=0, second=0, microsecond=0,
                                 tzinfo=timezone.utc).timestamp() * 1000))
    except Exception:
        return None


def build_properties(st: dict) -> dict:
    events = st.get("events", [])
    stage_evt = next((e for e in reversed(events) if e.get("action") == "stage_moved"), None)
    apple_evt = next((e for e in reversed(events) if e.get("action") in APPLE_ACTIONS), None)
    return {
        "amb_approval_stage": STAGE_LABEL.get(st.get("stage") or "", st.get("stage") or ""),
        "amb_stage_entered_date": _date_ms(stage_evt["at"]) if stage_evt else None,
        "amb_next_step_owner": st.get("owner") or "",
        "amb_last_apple_touch": _date_ms(apple_evt["at"]) if apple_evt else None,
    }


def cmd_map(brand, deal_id):
    st = _state(brand); st["hubspot_deal_id"] = str(deal_id); _save_state(brand, st)
    print(f"mapped {brand} → deal {deal_id}")


def cmd_ensure_props(write):
    existing = {p["name"] for p in _api("GET", "/crm/v3/properties/deals").get("results", [])}
    for name, label in PROPS.items():
        if name in existing:
            print(f"  ✓ {name} exists"); continue
        is_date = name.endswith("_date") or name.endswith("touch")
        spec = {"name": name, "label": label, "groupName": "dealinformation",
                "type": "date" if is_date else "string",
                "fieldType": "date" if is_date else "text"}
        if not write:
            print(f"  [dry-run] create {name} ({spec['type']})"); continue
        _api("POST", "/crm/v3/properties/deals", spec); print(f"  + created {name}")


def cmd_sync(brand, write):
    st = _state(brand)
    deal = st.get("hubspot_deal_id")
    props = {k: v for k, v in build_properties(st).items() if v not in (None, "")}
    if not deal:
        print(f"{brand}: no hubspot_deal_id mapped — run `map {brand} <deal_id>` first.")
        print(f"  would set: {props}")
        return
    if not write:
        print(f"[dry-run] PATCH deal {deal} ← {props}")
        return
    _api("PATCH", f"/crm/v3/objects/deals/{deal}", {"properties": props})
    print(f"synced deal {deal} ← {props}")


def cmd_note(brand, text, link, write):
    st = _state(brand); deal = st.get("hubspot_deal_id")
    body = text + (f"\n{link}" if link else "")
    if not deal:
        print(f"{brand}: no deal mapped. note would be: {body!r}"); return
    payload = {"properties": {"hs_note_body": body, "hs_timestamp": str(int(datetime.now(timezone.utc).timestamp() * 1000))},
               "associations": [{"to": {"id": deal}, "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 214}]}]}
    if not write:
        print(f"[dry-run] note on deal {deal}: {body!r}"); return
    _api("POST", "/crm/v3/objects/notes", payload); print(f"noted on deal {deal}")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    write = "--write" in a
    cmd = a[0]
    if cmd == "map": cmd_map(a[1], a[2])
    elif cmd == "ensure-props": cmd_ensure_props(write)
    elif cmd == "sync": cmd_sync(a[1], write)
    elif cmd == "note":
        link = a[a.index("--link") + 1] if "--link" in a else None
        cmd_note(a[1], a[2], link, write)
    else:
        print(f"unknown command {cmd!r}"); print(__doc__)


if __name__ == "__main__":
    main()
