#!/usr/bin/env python3
"""
Build a machine-readable index over the AMB canonical markdown so MSP integrators
can navigate, extract schemas, and map their platform code against AMB at scale.

Output: amb_index.json  (single self-describing artifact)
"""
import json, re, sys, datetime, hashlib

import os
SRC = os.environ.get("AMB_CANONICAL", "/mnt/user-data/uploads/AMB_Layer2_Canonical_v7_0.md")

# ---- provenance lookup (from the Source Inventory + Conflict/Recency table) ----
PROVENANCE = {
    "msp-rest-api":            {"rank":1,"version":"4.2.9","date":"2026-06-03","role":"Technical schema — top authority","stale":False},
    "apple-pay-merchant":      {"rank":2,"version":None,"date":"2026-03-01","role":"Apple Pay merchant setup/registration/processing","stale":False,"verification_note":"Part 3B byte-diffed 2026-07-08 against the source PDF: 98.5% lines matched; all residuals benign (TOC dot-leaders, PDF role-badge extraction garble, line reflow). No content loss; all JSON field names intact."},
    "messaging-documentation": {"rank":3,"version":"3.1","date":"2026-05-21","role":"Policy / UX / privacy / FAQ / metrics","stale":False},
    "msp-api-tutorial":        {"rank":4,"version":"3.4","date":"2026-04-29","role":"Worked examples / code","stale":False},
    "service-terms":           {"rank":5,"version":None,"date":"2024-12-17","role":"Legal layer","stale":False,"verification_note":"BYTE-VERIFIED 2026-07-08 against the complete source 'Service Terms for Messages for Business' (Dec 17 2024, captured from register.apple.com/tou/bca/latest/en — a multi-agreement page where the Service Terms is a section BELOW the Apple Business Register Terms of Use). 73/75 substantive lines match verbatim; the only 2 deviations are the canonical's two documented [sic] annotations (solely responsible maintaining §2.1; MESSSAGES §4.5), confirmed as deliberate inline additions, not drift. No dropped/reworded clauses, no fabrication, date matches. Part 4 fidelity flag RESOLVED."},
    "apple-pay-platform":      {"rank":6,"version":None,"date":"2025-06-01","role":"Apple Pay platform/PSP integration (superseded on overlap)","stale":False,"verification_note":"Part 3A byte-diffed 2026-07-08 against the source PDF: 96.9% lines matched; residuals benign (TOC dot-leaders, reflow). Cosmetic ligature-drop at canonical L10716 ('ll eld' -> 'fill field', Amex Token Block B row) FIXED. DATE RECONCILED 2026-07-09 to 2025-06-01 (June) to MATCH the canonical body: the guide's footer reads June 2025 while its cover reads September 2025; per the documented file-date protocol in §33.6 (file-internal footer date prevails over cover/catalog), June is authoritative. Index and body now agree on June; the earlier catalog value of 2025-09-01 (cover date) has been retired to resolve the index<->body mismatch."},
    "msp-onboarding":          {"rank":7,"version":"3.0.3","date":"2024-02-01","role":"MSP onboarding lifecycle","stale":True,"current_published_version":True,"stale_note":"v3.0.3 (01 Feb 2024) confirmed as Apple's CURRENT published version via live doc-rev-history (checked 2026-07-08) — NOT superseded; flagged stale only because it is materially older than sibling sources (2026). All five lifecycle sub-pages (mspRegistration, business-dev, integration, launch, postLaunch) cross-verified present & faithful against live portal pages on 2026-07-08. Per §37 R10, still cross-check uniquely-sourced step-level UI/timing, since Apple may edit a page without bumping the version."},
    "apple-business-register-tou": {"rank":None,"version":None,"date":"2024-10-15","role":"Legal — Apple Business Register Terms of Use","stale":False,"layer":"legal","verification_note":"Registered as a labeled legal source (C4). Full text is NOT inlined in this canonical body (unlike 'service-terms', which is byte-verified and consolidated in Part 4). Referenced by the canonical where brands accept terms via the Apple Business Register portal. Date set to 2024-10-15 from the source PDF's 'Last updated' stamp (Terms_of_Use_for_Apple_Business_Register.pdf, verified in this environment 2026-07-09). Distinct from the Service Terms (Dec 17 2024), which is a separate agreement stacked at the same register.apple.com/tou/bca/latest/en URL."},
    "amb-privacy":             {"rank":None,"version":None,"date":"2026-02-11","role":"Privacy — Apple Messages for Business privacy page","stale":False,"layer":"privacy","verification_note":"Registered as a labeled privacy source (C4). Full text is NOT inlined in this canonical body. Privacy behavior (e.g. opaque-ID, data handling) is described in prose within 'messaging-documentation' and Part 4; this entry catalogs the standalone AMB privacy page as a source. Date set to 2026-02-11 from the source capture's stamp (verified in this environment 2026-07-09)."},
    "overlay":                 {"rank":None,"version":"v7.0","date":"2026-07-01","role":"Master overlay (provenance/audit/registers) — not an Apple source","stale":False},
}

MESSAGE_TYPE_HINTS = [
    "quick reply","list picker","time picker","apple pay message","authentication message",
    "form message","text message","rich link","interactive message","received message","reply message",
]

def slugify(text, seen):
    # GitHub-flavored-markdown compatible anchor generation
    s = text.strip().lower()
    s = s.replace("&", "")
    # strip anything not alphanumeric, space or hyphen (removes emoji, em-dash, punctuation)
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    s = re.sub(r"[^a-z0-9\- ]", "", s)   # drop remaining non-ascii word chars
    s = s.strip().replace(" ", "-")
    s = re.sub(r"-+", "-", s)
    base = s
    if base in seen:
        seen[base] += 1
        s = f"{base}-{seen[base]}"
    else:
        seen[base] = 0
    return s

def main():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    n = len(lines)

    # ---- pass 1: locate headings, honoring code fences ----
    in_fence = False
    fence_tok = None
    heads = []  # (lineno_1based, level, title, raw)
    for i, ln in enumerate(lines):
        stripped = ln.lstrip()
        # fence toggling (``` or ~~~)
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m:
            tok = m.group(1)[0]
            if not in_fence:
                in_fence, fence_tok = True, tok
            elif fence_tok == tok:
                in_fence, fence_tok = False, None
            continue
        if in_fence:
            continue
        hm = re.match(r"^(#{1,6})\s+(.*\S)\s*$", ln)
        if hm:
            heads.append((i+1, len(hm.group(1)), hm.group(2).strip()))

    # ---- source-context tracker ----
    def source_for(title):
        t = title.lower()
        if t == "msp-rest-api": return "msp-rest-api"
        if t == "msp-api-tutorial": return "msp-api-tutorial"
        if t == "messaging-documentation": return "messaging-documentation"
        if t == "msp-onboarding": return "msp-onboarding"
        if "part 3a" in t or "platform integration guide" in t: return "apple-pay-platform"
        if "part 3b" in t or "merchant integration guide" in t: return "apple-pay-merchant"
        if "service terms" in t or "4. legal" in t: return "service-terms"
        if title.startswith("Appendix") or re.match(r"^\d+\.\s", title) is None and "canonical" in t:
            return "overlay"
        return None

    # domain (top-level Part) tracker via H2 "## N." headers and Appendix headers
    def domain_for(title):
        t = title.lower()
        if re.match(r"^1\.\s", title): return "API & Messages"
        if re.match(r"^2\.\s", title): return "Policy / UX / Privacy / Onboarding"
        if re.match(r"^3\.\s", title) or "apple pay" in t and title.startswith("Part 3"): return "Apple Pay"
        if re.match(r"^4\.\s", title): return "Legal (Service Terms)"
        if title.startswith("Appendix"): return "Overlay / Appendices"
        return None

    # compute section spans (end = line before next heading of level <= current)
    sections = []
    seen_slugs = {}
    cur_source = "overlay"
    cur_domain = None
    cur_part = None
    for idx,(lno, lvl, title) in enumerate(heads):
        s = source_for(title)
        if s: cur_source = s
        d = domain_for(title)
        if d: cur_domain = d
        if re.match(r"^Part\s", title) or re.match(r"^#*\s*Part\s", title):
            cur_part = title
        # end (subtree-inclusive)
        end = n
        for (l2,lv2,_) in heads[idx+1:]:
            if lv2 <= lvl:
                end = l2-1; break
        # own-content end (next heading of any level)
        own_end = n
        if idx+1 < len(heads):
            own_end = heads[idx+1][0]-1

        body = lines[lno:own_end]  # own content only (excl. the heading line)
        body_txt = "\n".join(body)

        # content signals over own content
        code_langs = sorted(set(
            (mm.group(1).lower() or "text")
            for mm in re.finditer(r"^\s*(?:```|~~~)([A-Za-z0-9_+-]*)", body_txt, re.M)
            if mm.group(1)
        ))
        has_code = bool(re.search(r"^\s*(?:```|~~~)", body_txt, re.M))
        has_table = bool(re.search(r"^\s*\|", body_txt, re.M))
        has_json = "json" in code_langs or bool(re.search(r"^\s*(?:```|~~~)\s*$", body_txt, re.M) and re.search(r'^\s*\{', body_txt, re.M))
        has_curl = any(x in code_langs for x in ("bash","sh","shell","curl")) or "curl -" in body_txt
        img_markers = re.findall(r"<!--\s*img:\s*([^\s>-][^>]*?)\s*-->", body_txt)
        img_markers = [x.strip() for x in re.findall(r"<!--\s*img:\s*(.+?)\s*-->", body_txt)]
        src_cites = re.findall(r"<sub>↳\s*`?([^`<\n]+?)`?\s*</sub>", body_txt)
        section_refs = sorted(set(re.findall(r"§\s?(\d+(?:\.\d+)*)", body_txt)))

        tl = title.lower()
        is_schema = tl.endswith("dictionary")
        is_message_type = (any(h in tl for h in MESSAGE_TYPE_HINTS)) and not is_schema
        is_endpoint = bool(re.match(r"^(sending|receiving|send |validating|authorizing|constructing|get |download)", tl)) or has_curl

        prov = PROVENANCE.get(cur_source, {})
        anchor = slugify(title, seen_slugs)

        sections.append({
            "seq": idx,
            "id": (re.match(r"^(\d+(?:\.\d+)*)", title).group(1) if re.match(r"^\d+", title) else None),
            "title": title,
            "level": lvl,
            "anchor": anchor,
            "line_start": lno,
            "line_end": end,
            "own_content_end": own_end,
            "line_count": end - lno + 1,
            "domain": cur_domain,
            "part": cur_part,
            "source": cur_source,
            "source_rank": prov.get("rank"),
            "source_version": prov.get("version"),
            "source_date": prov.get("date"),
            "source_stale": prov.get("stale", False),
            "flags": {
                "is_schema": is_schema,
                "is_message_type": is_message_type,
                "is_endpoint": is_endpoint,
                "has_code": has_code,
                "code_langs": code_langs,
                "has_json": has_json,
                "has_curl": has_curl,
                "has_table": has_table,
            },
            "img_markers": img_markers,
            "source_citations": src_cites,
            "cross_refs": section_refs,
        })

    # ---------- catalogs ----------
    # Nearest structural ancestor (strictly shallower heading, closest above).
    # Used to disambiguate duplicate schema names (e.g. 5x "Payment Dictionary").
    def parent_of(sec):
        p = None
        for other in sections:
            if other["line_start"] < sec["line_start"] and other["level"] < sec["level"]:
                p = other          # iterate in order; last qualifier = nearest ancestor
        return p

    def schema_entry(s):
        base = re.sub(r"\s+Dictionary$", "", s["title"], flags=re.I)
        par = parent_of(s)
        ptitle = par["title"] if par else None
        return {
            "name": base,
            # anchor is the guaranteed-unique machine key (slugify suffixes dupes);
            # qualified_name is the human-readable disambiguator.
            "qualified_name": f"{ptitle} \u203a {base}" if ptitle else base,
            "parent_title": ptitle,
            "title": s["title"], "anchor": s["anchor"],
            "line_start": s["line_start"], "line_end": s["line_end"],
            "source": s["source"], "part": s["part"],
        }
    schemas = [schema_entry(s) for s in sections if s["flags"]["is_schema"]]
    # Guarantee a human-unique qualified_name. Many schema headings (e.g. 5x
    # "Payment Dictionary") share a parent because Apple's message-type containers
    # ("Apple Pay Message", "Authentication Message") are bold prose, not headings.
    # For any colliding qualified_name, append the line marker so each is unique
    # and greppable. (anchor remains the guaranteed machine key regardless.)
    from collections import Counter as _C
    _dupe = {k for k, v in _C(x["qualified_name"] for x in schemas).items() if v > 1}
    for x in schemas:
        if x["qualified_name"] in _dupe:
            x["qualified_name"] = f"{x['qualified_name']} @L{x['line_start']}"

    message_types = [{"title": s["title"], "anchor": s["anchor"],
                      "line_start": s["line_start"], "line_end": s["line_end"],
                      "source": s["source"]}
                     for s in sections if s["flags"]["is_message_type"]]

    code_examples = [{"title": s["title"], "anchor": s["anchor"],
                      "line_start": s["line_start"], "line_end": s["line_end"],
                      "langs": s["flags"]["code_langs"], "source": s["source"]}
                     for s in sections if s["flags"]["has_code"]]

    # ---------- endpoints catalog (deterministic method+target scan) ----------
    # Apple's source renders "Authorizing Messages", "Sending a Message", etc. as
    # bold prose, not headings, so the procedural surface is invisible to sections[].
    # This scans every line for an HTTP verb + URL/path and pins it to its enclosing
    # section, giving integrators a navigable map of the actual API calls.
    def enclosing_section(lineno):
        best = None
        for s in sections:
            if s["line_start"] <= lineno <= s["line_end"]:
                if best is None or s["line_start"] > best["line_start"]:
                    best = s       # innermost (deepest-starting) enclosing section
        return best
    ep_re = re.compile(r"\b(POST|GET|PUT|DELETE|PATCH)\s+"
                       r"(https?://[^\s`\"'<>]+|/[A-Za-z0-9_][A-Za-z0-9_/{}.\-]*)")
    endpoints, seen_ep = [], set()
    for i, ln in enumerate(lines, start=1):
        for m in ep_re.finditer(ln):
            method = m.group(1)
            target = m.group(2).rstrip(".,);:")
            key = (method, target, i)
            if key in seen_ep:
                continue
            seen_ep.add(key)
            sec = enclosing_section(i)
            endpoints.append({
                "method": method, "target": target, "line": i,
                "section_title": sec["title"] if sec else None,
                "anchor": sec["anchor"] if sec else None,
                "source": sec["source"] if sec else None,
            })

    # ---------- parse audit gaps (§32.1) ----------
    def parse_md_table(start_hint_regex, cols):
        # find heading line, then read the first markdown table under it
        start = None
        for i,ln in enumerate(lines):
            if re.search(start_hint_regex, ln):
                start = i; break
        if start is None: return []
        rows=[]; header_seen=False
        for ln in lines[start:]:
            if ln.strip().startswith("|"):
                cells=[c.strip() for c in ln.strip().strip("|").split("|")]
                if set("".join(cells).replace("-","").replace(":","").strip())==set() and cells:
                    continue  # separator row
                if not header_seen:
                    header_seen=True; continue  # header row
                if len(cells)>=len(cols):
                    rows.append(dict(zip(cols, cells[:len(cols)])))
            elif header_seen and ln.strip()=="" :
                # allow blank lines inside? tables here have none; stop at first blank after data
                if rows: break
            elif header_seen and not ln.strip().startswith("|"):
                break
        return rows

    gaps = parse_md_table(r"^###\s*32\.1\s+Documentation Gaps",
                          ["num","topic","status","missing_detail","evidence_strength","spec_depth"])
    for g in gaps:
        g["num"] = g["num"].strip("* ")
        # FIX: classify by the leading status marker, not a naive substring.
        # The old test  ("resolved" in status.lower())  also matched the string
        # "⚠️ Unresolved", so every genuinely-open gap was flagged resolved=True,
        # hiding 6 of the 7 real open decision points. Every row carries exactly
        # one marker: ✅ (closed) or ⚠️ (open/partial). Key off that.
        st = g["status"].strip()
        g["resolved"] = ("✅" in st) and ("⚠️" not in st)
        g["open_decision_point"] = (not g["resolved"]) and ("No Spec" in g["spec_depth"])
    conflicts = parse_md_table(r"^##\s*37\.\s+CONFLICT",
                          ["ref","topic","chosen_value","winning_source","superseded_value","note"])
    for c in conflicts:
        c["ref"] = c["ref"].strip("* ")

    provenance_out = [{"key":k, **v} for k,v in PROVENANCE.items()]

    meta = {
        "canonical_file": "AMB_Layer2_Canonical_v7_0.md",
        "canonical_version": "v7.0-verbatim-consolidated",
        "assembled": "2026-07",
        "index_generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_lines": n,
        "section_count": len(sections),
        "schema_count": len(schemas),
        "message_type_count": len(message_types),
        "code_example_count": len(code_examples),
        "endpoint_count": len(endpoints),
        "gap_count": len(gaps),
        "open_decision_point_count": sum(1 for g in gaps if g["open_decision_point"]),
        "conflict_count": len(conflicts),
        "anchor_convention": "GitHub-flavored-markdown slug (lowercase, punctuation stripped, spaces->hyphens, duplicates suffixed -1,-2...)",
        "line_numbers": "1-based, inclusive; line_end is subtree-inclusive (covers child sections)",
        "notes": [
            "Anchors assume this file is rendered by a GFM-compatible renderer; verify against your host portal.",
            "source='service-terms' (Part 4/Legal) was self-flagged in the canonical as reconstructed-from-paste pending byte-diff. RESOLVED 2026-07-08: byte-verified against the complete Apple source (Dec 17 2024); only deviations are the 2 documented [sic] annotations. See provenance.service-terms.verification_note.",
            "source_stale=true (msp-onboarding, 2024) means uniquely-sourced facts need verification per the canonical's own rule (§37 R10).",
            "catalogs.endpoints[].line is the exact 1-based location and is authoritative; section_title/anchor are the nearest enclosing heading. Because Apple renders some procedure titles (e.g. 'Downloading and Decrypting an Attachment') as bold prose rather than headings, an endpoint's nearest heading may be the preceding sibling — use line to locate the exact call.",
            "catalogs.schemas[].anchor is the unique machine key; qualified_name is the human label (line marker appended where names collide)."
        ],
    }

    out = {
        "meta": meta,
        "provenance": provenance_out,
        "sections": sections,
        "catalogs": {
            "schemas": schemas,
            "message_types": message_types,
            "code_examples": code_examples,
            "endpoints": endpoints,
            "gaps": gaps,
            "conflict_register": conflicts,
        },
        "anchor_lookup": {s["anchor"]: s["seq"] for s in sections},
    }

    with open(os.environ.get("AMB_INDEX", os.path.join(os.path.dirname(os.path.abspath(__file__)),"amb_index.json")),"w",encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # quick console report
    print("sections:", len(sections))
    print("schemas:", len(schemas))
    print("message_types:", len(message_types))
    print("code_examples:", len(code_examples))
    print("endpoints:", len(endpoints))
    print("gaps parsed:", len(gaps))
    print("open decision points:", sum(1 for g in gaps if g["open_decision_point"]))
    print("conflicts parsed:", len(conflicts))
    print("sample schema:", schemas[0] if schemas else None)
    print("sample gap:", {k:(v[:60]+'...' if isinstance(v,str) and len(v)>60 else v) for k,v in gaps[0].items()} if gaps else None)
    print("dup anchor spot-check (Payment Dictionary variants):",
          [s["anchor"] for s in sections if s["title"]=="Payment Dictionary"][:6])

if __name__=="__main__":
    main()
