"""
Storyboard rule validation (the cheap place to catch Apple's big fails — before
anything is built). Blocker-level rules refuse a clean render; warnings are noted.
Rules trace to the rule set (ids in parentheses).
"""
from __future__ import annotations
import re

RICH = {"list_picker", "time_picker", "apple_pay", "auth", "rich_link"}
BARE_URL = re.compile(r"\b[a-z0-9-]+\.(com|io|co|ai|net|org)(/\S*)?\b", re.I)
PERSON = re.compile(r"\b(person|agent|representative|specialist|human|someone)\b", re.I)
AUTO = re.compile(r"\b(automated|assistant|bot|virtual)\b", re.I)
ANYTHING_ELSE = re.compile(r"anything else|help with anything|is there anything", re.I)
OOH = re.compile(r"\b(offline|out[- ]of[- ]hours|off[- ]hours|closed|hours:|not available)\b", re.I)


def _f(flow, i, sev, rule, msg):
    return {"flow": flow, "step": i, "severity": sev, "rule": rule, "msg": msg}


def validate_model(model: dict) -> list[dict]:
    """Validate the review-driven slide model (sections/steps/screens)."""
    issues = []
    sections = model.get("sections", [])
    all_text = " ".join(
        (b.get("text", "") for s in sections for st in s.get("steps", [])
         for b in (st.get("screen", {}) or {}).get("bubbles", []) or [])).lower()
    # welcome self-identifies as automated + explains HELP/STOP
    signup = next((s for s in sections if "sign" in (s.get("id", "") + s.get("title", "")).lower()
                   or "welcome" in (s.get("title", "")).lower()), None)
    welcome_text = ""
    if signup:
        welcome_text = " ".join(b.get("text", "") for st in signup.get("steps", [])
                                for b in (st.get("screen", {}) or {}).get("bubbles", []) or []).lower()
    if not AUTO.search(welcome_text or all_text):
        issues.append(_f("signup", 0, "blocker", "3.2", "Welcome doesn't self-identify as an automated assistant."))
    if "help" not in (welcome_text or all_text) or "stop" not in (welcome_text or all_text):
        issues.append(_f("signup", 0, "warn", "10.8", "Welcome should explain HELP (reach a person) and STOP (opt out)."))
    # framing before every rich element + person route + out-of-hours
    for s in sections:
        steps = s.get("steps", [])
        for i, st in enumerate(steps):
            el = (st.get("screen", {}) or {}).get("element")
            if el and el in RICH:
                prev = steps[i - 1] if i >= 1 else None
                prev_txt = " ".join(b.get("text", "") for b in ((prev or {}).get("screen", {}) or {}).get("bubbles", []) or [])
                if not prev_txt.strip():
                    issues.append(_f(s.get("id", "?"), i + 1, "blocker", "4.5", f"No framing bubble before the {el}."))
    if not PERSON.search(all_text):
        issues.append(_f("all", 0, "blocker", "9.1", "No route to a person shown anywhere."))
    if not OOH.search(all_text) and "stop" not in all_text:
        issues.append(_f("all", 0, "warn", "3.18", "No out-of-hours / opt-out path shown."))
    return issues


def validate(flow_data: dict) -> list[dict]:
    issues = []
    flows = flow_data.get("flows", {})

    for fkey, steps in flows.items():
        bot_steps = [(i, s) for i, s in enumerate(steps, 1) if s.get("actor") in ("bot", "human")]
        # 1. automated disclosure in the opener (flow A)
        if fkey == "A" and bot_steps:
            i0, s0 = bot_steps[0]
            if not AUTO.search(s0.get("copy", "")):
                issues.append(_f(fkey, i0, "blocker", "3.2", "Opener must disclose it's an automated assistant."))
        # per-step checks
        menus = 0
        for i, s in enumerate(steps, 1):
            k, copy = s["kind"], s.get("copy", "")
            # 5. no bare URL
            if BARE_URL.search(copy):
                issues.append(_f(fkey, i, "blocker", "4.1", f'Bare URL in copy ("{BARE_URL.search(copy).group(0)}") — use a Rich Link.'))
            # 2 + 6. quick reply / list picker sizing
            if k == "quick_reply":
                menus += 1
                n = len(s.get("options", []))
                if n > 5:
                    issues.append(_f(fkey, i, "blocker", "5.4", f"Quick Reply has {n} options (>5) — use a List Picker."))
            if k == "list_picker":
                menus += 1
                n = len(s.get("options", []))
                if n <= 5:
                    issues.append(_f(fkey, i, "warn", "5.4", f"List Picker has {n} options (<=5) — a Quick Reply fits better."))
            # 3. framing before every rich element
            if k in RICH:
                prev = steps[i - 2] if i >= 2 else None
                if not (prev and prev.get("actor") == "bot" and prev["kind"] in ("framing", "text")):
                    issues.append(_f(fkey, i, "blocker", "4.5", f"No framing bubble before the {k}."))
            # 4. confirmation after a tap (customer selecting after a rich element)
            if s.get("actor") == "customer" and i >= 2 and steps[i - 2]["kind"] in RICH:
                nxt = steps[i] if i < len(steps) else None
                if not (nxt and nxt.get("actor") == "bot" and nxt["kind"] in ("text", "framing")):
                    issues.append(_f(fkey, i, "blocker", "5.6", "No confirmation bubble after the customer's selection."))

        # 7. route to a person on the main menu (flow A)
        if fkey == "A":
            has_person = any(PERSON.search(o) for s in steps if s["kind"] in ("quick_reply", "list_picker")
                             for o in s.get("options", []))
            if menus and not has_person:
                issues.append(_f(fkey, 0, "blocker", "9.1", "No route to a person on any menu."))
            # 8. anything-else before close
            tail = " ".join(s.get("copy", "") for s in steps[-2:])
            if not ANYTHING_ELSE.search(tail):
                issues.append(_f(fkey, len(steps), "warn", "10.9", 'No "anything else" prompt before the conversation closes.'))

    # 9. out-of-hours + fallback path present (flow C)
    cflow = flows.get("C", [])
    if not cflow:
        issues.append(_f("C", 0, "blocker", "3.18", "No degraded/out-of-hours flow (Flow C) provided."))
    elif not any(OOH.search(s.get("copy", "")) for s in cflow):
        issues.append(_f("C", 0, "blocker", "3.18", "Flow C does not show an out-of-hours / offline message."))

    return issues
