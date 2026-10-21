#!/usr/bin/env python3
"""
build_openapi.py — Assemble a VALIDATED OpenAPI 3.1 skeleton from the AMB
endpoints catalog in amb_index.json.

Honesty scope: paths, methods, servers, operationIds and provenance
(x-amb-source line + enclosing section) are deterministic and correct.
Request/response bodies are wired to the extracted schema bundle ONLY where the
mapping is unambiguous (e.g. POST /message -> the interactive-message envelope);
everywhere else the operation carries a described placeholder plus the exact
canonical line to read, rather than a guessed body. Apple-hosted calls become
`paths`; MSP-/merchant-hosted calls (which the integrator implements and Apple
invokes) become OpenAPI 3.1 `webhooks`.

Output: amb.openapi.json
"""
import json, re, datetime, sys, os
from pathlib import Path
from urllib.parse import urlsplit

ROOT  = Path(__file__).resolve().parent
_def_index = ROOT / "amb_index.json"
if not _def_index.exists():
    _def_index = Path("/mnt/user-data/uploads/amb_index.json")
INDEX = Path(os.environ.get("AMB_INDEX", str(_def_index)))
BUNDLE_ID = "amb_schemas_bundle.json"   # A1: single canonical filename (underscores)

# Which hosts are Apple-hosted (integrator CALLS these) vs integrator-hosted
# (integrator IMPLEMENTS these; Apple/merchant calls them -> webhooks).
APPLE_HOSTS = {"mspgw.push.apple.com", "apple-pay-gateway.apple.com"}

SERVER_ROLE = {
    "mspgw.push.apple.com":        "Apple Messages for Business REST gateway (MSP calls these).",
    "apple-pay-gateway.apple.com": "Apple Pay gateway (merchant/PSP calls these).",
    "msp.example.com":             "MSP-hosted callback surface (the integrator implements; Apple calls it).",
    "merchant.example.com":        "Merchant-hosted notification surface (the integrator implements).",
}

def message_body_schema():
    """A2: the real POST /message body is the HTTP Body envelope; the interactive
    path additionally carries interactiveData (interactive messages inherit from
    HTTP Body, canonical L419). Modelled faithfully with allOf so HTTP Body stays
    exactly its 9 source fields and interactiveData is an explicit extension."""
    return {"allOf": [
        {"$ref": f"{BUNDLE_ID}#/$defs/http-body"},
        {"type": "object",
         "properties": {"interactiveData": {"$ref": f"{BUNDLE_ID}#/$defs/baseinteractivemessage-dictionary"}},
         "description": "Present when type=interactive. Interactive messages inherit from "
                        "HTTP Body (canonical L419); verify exact interactiveData nesting there."}
    ]}

# Custom request-body builders keyed by (method, normalized-path).
BODY_BUILDER = {
    ("POST", "/message"): message_body_schema,
}

def opid(method, path):
    parts = re.findall(r"[A-Za-z0-9]+", path)
    tail = "".join(p.capitalize() for p in parts) or "Root"
    return method.lower() + tail

def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    eps = idx["catalogs"]["endpoints"]

    servers_seen = {}      # host -> server url base
    paths = {}             # path -> {method -> operation}
    webhooks = {}          # name -> {method -> operation}
    seen = set()           # dedupe (method, host, path)

    for e in eps:
        method, target, line = e["method"], e["target"], e["line"]
        u = urlsplit(target)
        host = u.netloc
        path = u.path or target
        # bare relative targets ("/message") have no host; treat as Apple gateway
        if not host:
            host = "mspgw.push.apple.com"
        key = (method, host, path)
        if key in seen:
            continue
        seen.add(key)

        base = f"{u.scheme or 'https'}://{host}" + (
            "/v1" if host == "mspgw.push.apple.com" and not path.startswith("/v1") else "")
        # normalize path so it doesn't double the /v1
        norm_path = path
        if host == "mspgw.push.apple.com":
            norm_path = re.sub(r"^/v1", "", path) or "/"
            base = f"https://{host}/v1"
        servers_seen.setdefault(host, base)

        path_params = re.findall(r"\{([^}]+)\}", norm_path)
        op = {
            "operationId": opid(method, norm_path),
            "summary": e.get("section_title") or f"{method} {norm_path}",
            "description": (
                f"Derived from the AMB canonical at line {line} "
                f"(section: {e.get('section_title')}, source: {e.get('source')}). "
                "Verify request/response bodies against that location before relying."),
            "x-amb-source": {
                "canonical_line": line,
                "section_title": e.get("section_title"),
                "section_anchor": e.get("anchor"),
                "source": e.get("source"),
            },
            "responses": {
                "200": {"description": "See canonical at the x-amb-source line for the exact response shape."}
            },
        }
        if path_params:
            op["parameters"] = [
                {"name": p, "in": "path", "required": True,
                 "schema": {"type": "string"},
                 "description": f"Path parameter '{p}' (see canonical L{line})."}
                for p in path_params
            ]
        if method in ("POST", "PUT", "PATCH"):
            builder = BODY_BUILDER.get((method, norm_path))
            if builder:
                op["requestBody"] = {"required": True,
                    "content": {"application/json": {"schema": builder()}}}
            else:
                op["requestBody"] = {
                    "content": {"application/json": {"schema": {
                        "type": "object",
                        "description": "Body shape not auto-mapped; read the canonical "
                                       f"at line {line} and wire the correct schema from "
                                       f"{BUNDLE_ID}.",
                    }}},
                }

        if host in APPLE_HOSTS:
            paths.setdefault(norm_path, {})[method.lower()] = op
        else:
            wh_name = opid(method, norm_path)
            webhooks.setdefault(wh_name, {})[method.lower()] = op

    servers = [{"url": url, "description": SERVER_ROLE.get(host, host)}
               for host, url in sorted(servers_seen.items()) if host in APPLE_HOSTS]

    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": "Apple Messages for Business — MSP API (skeleton)",
            "version": "derived-from-canonical-" + idx["meta"]["canonical_version"],
            "summary": "Deterministically derived endpoint skeleton. Not an Apple-published spec.",
            "description": (
                "Auto-assembled from the endpoints catalog of amb_index.json. Paths, methods, "
                "servers and provenance are exact; bodies are wired only where unambiguous and "
                "otherwise carry the canonical line to read. Integrator-implemented callbacks "
                "(MSP/merchant-hosted) are modelled as `webhooks`."),
            "x-amb-generator": {
                "tool": "build_openapi.py",
                "canonical": idx["meta"]["canonical_file"],
                "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            },
        },
        "servers": servers,
        "paths": paths,
        "webhooks": webhooks,
    }

    # ---- A1: explicit external $ref existence check ----------------------
    # openapi-spec-validator does NOT verify that "<file>#/..." targets exist.
    # Confirm every referenced bundle file is on disk AND the $defs anchor exists.
    bundle_path = ROOT / BUNDLE_ID
    ref_errors = []
    ext_refs = re.findall(r'"([^"#]+\.json)#/\$defs/([^"]+)"', json.dumps(spec))
    bundle_defs = set()
    if bundle_path.exists():
        bundle_defs = set(json.loads(bundle_path.read_text()).get("$defs", {}).keys())
    else:
        ref_errors.append(f"bundle file missing: {BUNDLE_ID}")
    for fname, anchor in ext_refs:
        if not (ROOT / fname).exists():
            ref_errors.append(f"$ref target file not found: {fname}")
        elif anchor not in bundle_defs:
            ref_errors.append(f"$ref anchor not in {fname}: #/$defs/{anchor}")

    # ---- OpenAPI 3.1 structural validation -------------------------------
    from openapi_spec_validator import validate
    spec_error = None
    try:
        validate(spec)
    except Exception as e:
        spec_error = str(e)[:300]

    # ---- self-validate: refuse to emit on any failure --------------------
    if ref_errors or spec_error:
        print("ABORT: OpenAPI not written.", file=sys.stderr)
        for e in ref_errors:
            print(f"  external-ref: {e}", file=sys.stderr)
        if spec_error:
            print(f"  spec: {spec_error}", file=sys.stderr)
        sys.exit(1)

    (ROOT / "amb.openapi.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"servers:  {len(servers)}")
    for s in servers: print("   ", s["url"])
    print(f"paths:    {len(paths)}  (operations: {sum(len(v) for v in paths.values())})")
    print(f"webhooks: {len(webhooks)} (integrator-implemented callbacks)")
    print(f"external $refs checked: {len(ext_refs)}  (all resolve)")
    print(f"openapi 3.1 validation: VALID")

if __name__ == "__main__":
    main()
