"""
Terminology lint (rule 0.3 + Apple onboarding naming rules). Shared by Tool 1
(the brand doc + filenames) and available to Tools 2/3. Flags customer-facing
copy that uses forbidden platform wording or implies Apple endorsement.
"""
from __future__ import annotations
import re
from dataclasses import dataclass

# (pattern, message, suggestion). "chat"/"text" are only flagged as a channel NAME,
# so they are handled with a narrower pattern to avoid false positives on verbs.
RULES = [
    (re.compile(r"\bi-?message(s)?\b(?!\s*&\s*facetime)", re.I),
     'Uses "iMessage"', 'Use "Apple Messages for Business"'),
    (re.compile(r"\bapple chat\b", re.I), 'Uses "Apple Chat"', 'Use "Apple Messages for Business"'),
    (re.compile(r"\bAMB\b"), 'Uses the "AMB" abbreviation', 'Spell out "Apple Messages for Business"'),
    (re.compile(r"\bimessage app\b", re.I),
     'Labels a feature "iMessage app"', 'Use "App Extension" / "embedded app experience"'),
    (re.compile(r"\b(first|only|exclusive|selected)\s+(msp|partner)\b", re.I),
     "Exclusivity claim", "Remove exclusivity/endorsement claims"),
    (re.compile(r"\bselected by apple\b|\bapple('s)? (chosen|preferred|endorsed)\b", re.I),
     "Implies Apple endorsement", "Do not imply Apple endorses the brand"),
    (re.compile(r"\b(our|the)\s+(chat|text)\s+(channel|service|experience)\b", re.I),
     'Uses "chat"/"text" as the channel name', 'Name the channel "Apple Messages for Business"'),
]


@dataclass
class Hit:
    rule: str
    match: str
    suggestion: str
    where: str  # field name / location label


def lint(text: str, where: str = "") -> list[Hit]:
    hits = []
    for rx, msg, fix in RULES:
        for m in rx.finditer(text or ""):
            hits.append(Hit(rule=msg, match=m.group(0), suggestion=fix, where=where))
    return hits


def lint_fields(values: dict[str, str]) -> list[Hit]:
    out = []
    for field, val in values.items():
        if isinstance(val, str):
            out.extend(lint(val, where=field))
    return out


if __name__ == "__main__":
    sample = 'An iMessage app brings the Walmart app gallery into the chat. First MSP selected by Apple.'
    for h in lint(sample, "demo"):
        print(f"  [{h.where}] {h.rule}: {h.match!r} → {h.suggestion}")
