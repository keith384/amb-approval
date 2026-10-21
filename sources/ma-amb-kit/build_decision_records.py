#!/usr/bin/env python3
"""
build_decision_records.py — C3. Emit one decision-record (DR) per OPEN DECISION
POINT (gaps flagged open_decision_point in amb_index.json). Apple is silent on
these, so each becomes the integrator's own policy.

Faithfulness: the *context* of each DR is pulled verbatim-ish from the index gap
(topic + Apple's documented silence), so it stays synced to the canonical. The
*options / trade-offs / recommended default* are explicitly labeled INTEGRATOR
POLICY RECOMMENDATIONS — engineering guidance, NOT Apple specification. Nothing
here asserts Apple behavior Apple hasn't stated.

Output: decision_records/DR-<num>-<slug>.md  + decision_records/README.md
"""
import json, os, re, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
_def_index = ROOT / "amb_index.json"
if not _def_index.exists():
    _def_index = Path("/mnt/user-data/uploads/amb_index.json")
INDEX = Path(os.environ.get("AMB_INDEX", str(_def_index)))
OUT = ROOT / "decision_records"
OUT.mkdir(exist_ok=True)

def slug(t):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")

# Curated engineering guidance per topic. Keyed by gap num. These are RECOMMENDATIONS,
# not Apple spec. Each: options [(label, note)], recommended default, and notes.
GUIDANCE = {
    "2": {  # TLS version
        "options": [
            ("TLS 1.2 only", "Matches the one version Apple documents as required. Simplest to certify; forgoes 1.3's latency/security gains."),
            ("TLS 1.2 + 1.3 (recommended)", "Negotiate 1.3, fall back to 1.2. Apple documents 1.2 as the floor and is silent on 1.3, so offering both is safe and forward-compatible."),
            ("Require TLS 1.3", "Rejected: Apple only guarantees 1.2 on the relay; forcing 1.3 risks handshake failures."),
        ],
        "default": "Support TLS 1.3 and 1.2; disable everything below 1.2. Pin the documented 1.2 requirement as the hard floor.",
        "notes": "Re-check on each Apple relay change; the 1.3 question is unresolved upstream (gap #2).",
    },
    "3": {  # at-rest crypto
        "options": [
            ("AES-256-GCM at rest (recommended)", "Authenticated encryption for cached/queued messages; widely certifiable (FIPS 140-2/3)."),
            ("Envelope encryption via cloud KMS", "Per-record data keys wrapped by a KMS master key; strong key rotation and audit story."),
            ("No at-rest encryption", "Rejected: message bodies contain user content; unencrypted cache is a compliance and breach risk."),
        ],
        "default": "AES-256-GCM with keys held in a managed KMS; rotate master keys; encrypt any message cache, attachment blob, and queue.",
        "notes": "Apple specifies no at-rest algorithm (gap #3); this is entirely MSP policy. Aligns with the ISO 27001/27018 posture Apple does cite.",
    },
    "11": {  # Managed Apple Account
        "options": [
            ("Treat like a standard Apple Account", "Simplest; assumes identical AMB message flow. Risk: Managed accounts may have org-imposed restrictions Apple hasn't documented for AMB."),
            ("Support with documented caveats (recommended)", "Enable, but sandbox-test the full lifecycle and surface any org-policy limitations to the brand."),
            ("Block Managed accounts", "Rejected without evidence they misbehave; over-restrictive."),
        ],
        "default": "Support Managed Apple Accounts; verify opaque-ID issuance, opt-out, and attachment flows in sandbox before GA; document any observed differences.",
        "notes": "Onboarding docs confirm a Managed account may be used for AMB login, but per-message behavior is unspecified (gap #11). Verify, don't assume.",
    },
    "13": {  # read receipts
        "options": [
            ("Do not surface read receipts (recommended)", "Apple documents read receipts for person-to-person iMessage, not AMB business context. Treat delivery (200 OK) as the only confirmed signal."),
            ("Surface optimistically", "Rejected: would assert a 'read' state Apple does not confirm delivering for AMB — misleading to agents."),
            ("Make it a per-brand toggle", "Acceptable if defaulted OFF and clearly labeled 'delivery, not read'."),
        ],
        "default": "Do not display 'read' status in the agent console for AMB. Map the 200-OK response to 'delivered'. Revisit if Apple documents AMB read receipts.",
        "notes": "No AMB business-context read-receipt spec exists (gap #13). Delivery ≠ read.",
    },
    "15": {  # rate limits
        "options": [
            ("No self-imposed limits", "Rejected: unbounded send risks 5xx storms and brand-level throttling Apple may apply without publishing thresholds."),
            ("Static conservative caps", "Per-brand and per-conversation ceilings set well below any plausible Apple limit; predictable but may under-utilize."),
            ("Adaptive backoff + conservative caps (recommended)", "Honor the documented 5xx retry behavior (Apple retries 4x with exponential backoff from 100ms), add 429-aware client-side throttling, and cap per-brand/per-conversation."),
        ],
        "default": "Adaptive: conservative per-brand + per-conversation caps, exponential backoff on 5xx/429 (start 100ms, ~4 retries, matching Apple's documented server retry), and a global send budget with circuit-breaking.",
        "notes": "Apple publishes no rate-limit table (gap #15). The only documented timing signal is the 5xx retry policy in the Response Codes section; anchor client behavior to it.",
    },
    "16": {  # geographic availability
        "options": [
            ("Allow all regions", "Rejected: AMB availability is Apple-ecosystem and country-gated; sending into unsupported regions yields silent failures."),
            ("Allowlist from onboarding (recommended)", "Maintain a supported-country allowlist sourced from Apple Business Register brand onboarding; deny/queue elsewhere with a clear fallback."),
            ("Geo-gate at the edge", "Acceptable as an enforcement mechanism layered on the allowlist."),
        ],
        "default": "Maintain a per-brand supported-region allowlist derived from Apple Business Register onboarding; on out-of-region targets, fail gracefully with a documented fallback channel.",
        "notes": "No Apple-authored country list exists (gap #16); availability is confirmed only as Apple-ecosystem-only. Treat the allowlist as living config.",
    },
    "18": {  # SOC 2
        "options": [
            ("Rely on ISO 27001/27018 only", "Apple cites ISO 27001 and 27018 for its own posture; an MSP may inherit that framing but it is not SOC 2."),
            ("Pursue SOC 2 Type II (recommended where enterprise-required)", "Independent attestation many enterprise brands demand from an MSP; complements ISO."),
            ("Both ISO + SOC 2", "Strongest assurance story; higher audit cost."),
        ],
        "default": "Document the ISO 27001/27018 baseline Apple references; pursue SOC 2 Type II if your target brands require it in procurement. State clearly that AMB itself carries no Apple-published SOC 2 claim.",
        "notes": "SOC 2 is not addressed in any Apple source (gap #18); ISO 27001/27018 are confirmed. This is an MSP business/compliance decision.",
    },
}

def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    dps = [g for g in idx["catalogs"]["gaps"] if g.get("open_decision_point")]
    if not dps:
        print("ABORT: no open decision points found in index.", file=sys.stderr); sys.exit(1)

    written = []
    for g in dps:
        num = g["num"]
        gd = GUIDANCE.get(num)
        s = slug(g["topic"])
        fn = f"DR-{num.zfill(2)}-{s}.md"
        md = []
        md.append(f"# Decision Record DR-{num}: {g['topic']}\n")
        md.append(f"_Status: **OPEN — integrator must decide.** Generated {datetime.datetime.now(datetime.timezone.utc).date()} "
                  f"from amb_index.json gap #{num}._\n")
        md.append("> **These options and the recommended default are INTEGRATOR POLICY "
                  "RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is "
                  "silent on this point (see Context), so the behavior becomes your platform's own policy.\n")
        md.append("## Context (what Apple does / does not say)\n")
        md.append(f"- **Topic:** {g['topic']}")
        md.append(f"- **Apple's silence:** {g['missing_detail']}")
        md.append(f"- **Evidence strength (per canonical):** {g.get('evidence_strength','—')}")
        md.append(f"- **Specification depth:** {g.get('spec_depth','—')}\n")
        if gd:
            md.append("## Options\n")
            for label, note in gd["options"]:
                md.append(f"- **{label}** — {note}")
            md.append("\n## Recommended default\n")
            md.append(f"{gd['default']}\n")
            md.append("## Notes\n")
            md.append(f"{gd['notes']}\n")
        else:
            md.append("## Options\n\n_TODO: enumerate options, trade-offs, and a default._\n")
        md.append("## Decision (fill in)\n")
        md.append("- **Chosen option:** _____\n- **Owner / date:** _____\n- **Rationale:** _____\n"
                  "- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.\n")
        (OUT / fn).write_text("\n".join(md), encoding="utf-8")
        written.append((num, g["topic"], fn))

    # index
    rd = ["# Decision Records — Open Decision Points\n",
          f"_Generated {datetime.datetime.now(datetime.timezone.utc).isoformat()} from "
          f"{len(written)} open decision points in amb_index.json._\n",
          "Apple specifies nothing on these; each is the integrator's own policy. Options and "
          "defaults are recommendations, not Apple spec.\n",
          "| DR | Topic | File |", "|---|---|---|"]
    for num, topic, fn in written:
        rd.append(f"| DR-{num} | {topic} | [`{fn}`](./{fn}) |")
    (OUT / "README.md").write_text("\n".join(rd), encoding="utf-8")

    print(f"decision records written: {len(written)}  -> decision_records/")
    for num, topic, fn in written:
        print(f"  DR-{num}: {topic}")

if __name__ == "__main__":
    main()
