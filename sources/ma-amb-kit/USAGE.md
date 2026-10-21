# How to Use and Maintain the AMB Kit

*Written to be followed even if you don't work with code, repositories, or the
command line. Where a step genuinely needs a developer or a tool, it says so plainly
and gives you a way to hand it off.*

---

## 1. The one idea to hold onto

There is **one file you ever edit by hand**: the canonical,
`AMB_Layer2_Canonical_v7_0.md`. It is the single source of truth — every Apple rule,
schema, payload, and legal term, verified against Apple's originals.

**Everything else in the folder is *generated* from that canonical by a script.** The
schemas, the index, the OpenAPI file, the fixtures, the conformance checklist, the
decision records, the reference — you never edit those by hand. When Apple changes
something, you edit the canonical and re-run one command, and all the generated files
refresh themselves.

So the whole system is: **edit the canonical → run one command → everything else updates.**
That's it. If you remember nothing else, remember that.

---

## 2. Which files to keep, and which to delete (read this first)

You now have several copies of things floating around from different work sessions.
Here is how to clean that up so you never get confused again:

**KEEP exactly one thing: `amb_kit_full.zip`.**
Unzip it once into a folder (call it `amb-kit`). **That folder is the entire project.**
It already contains the corrected canonical, all the generated files, and all the
scripts. It is the newest and most correct version of everything.

**DELETE (or archive in a separate "old" folder) everything else you downloaded loose**,
because they are older, superseded copies that now live — corrected — inside the zip:

- Any loose `amb_index.json`, `build_index.py`, `amb_schemas_bundle.json`,
  `amb_openapi*.json`, `conformance_checklist.md`, `schema_coverage_report*.md`,
  `README*.md`, `fixtures_validation.md`, `build_all.py` sitting outside the folder.
- Any `schemas.zip` or `decision_records.zip` — those contents are already inside the
  full kit.

> **Why this matters:** if you keep old loose files next to the folder, you might one day
> run an *old* script or point a tool at a *stale* schema, and get wrong results with no
> warning. One folder, from the zip, nothing else beside it. That single rule prevents
> 90% of the confusion.

The two extra files that came alongside the zip in the same delivery
(`amb_index.json` and `build_index.py` on their own) are **just previews** — identical
copies of files already inside the zip. You can ignore or delete them.

---

## 3. What's in the box (in plain language)

| Thing | What it's for |
|---|---|
| `AMB_Layer2_Canonical_v7_0.md` | The source of truth. The full, verified Apple documentation. The only file you edit. |
| `AMB_Schemas_Reference.md` | A human-readable list of every data structure ("schema") Apple defines, with its fields. Good for reading and citing. |
| `amb_index.json` | The "map." Lets a tool or an AI jump straight to the right section instead of reading the whole thing. |
| `schemas/` + `amb_schemas_bundle.json` | The machine-readable version of Apple's data structures — used by developers to check that a message is built correctly. |
| `amb.openapi.json` | A standard description of Apple's web endpoints — used by developers to generate code or test tools. |
| `fixtures/` + `fixtures_validation.md` | Real example messages from Apple's docs, plus a report checking them against the schemas. |
| `conformance_checklist.md` | Apple's required features, each mapped to the relevant schema/endpoint. This is close to Apple's approval checklist. |
| `decision_records/` | Seven things Apple deliberately does **not** specify (rate limits, encryption-at-rest, etc.), which become *your* policy — with a recommended default for each. |
| `schema_coverage_report.md` | The honesty log: every place Apple's source was unclear and the tool refused to guess. |
| `build_all.py` and the other `.py` files | The machinery that regenerates everything from the canonical. You run one of them; the rest run automatically. |
| `README.md`, `README_schemas.md`, this `USAGE.md` | The written guides. |

---

## 4. Where to put it

Put the unzipped `amb-kit` folder somewhere permanent and backed-up — your Documents
folder synced to iCloud/OneDrive/Dropbox is fine to start. You do **not** need GitHub or
"a repo" to use it. (If you later bring on a developer, they'll likely put it in Git, and
that's great — but it's not required for you to work.)

Keep the whole folder together. The scripts expect their neighbours to be in the same
folder.

---

## 5. Using it — three ways, easiest first

### Method 1 — Content generation with a Claude Project (no command line, this is the main one)

This replaces what you were doing before (pasting the whole canonical into a chat). It's
fully within reach and is how you'll work day-to-day.

**Setup (once):**
1. In Claude, create a **Project** (Projects keep a set of files available to every chat
   inside them, so you don't re-upload each time).
2. Upload the **compact** files into the Project's knowledge — *not* the giant canonical:
   - `AMB_Schemas_Reference.md`
   - `amb_index.json`
   - `conformance_checklist.md`
   - the `decision_records/` files
   - `README.md`
   Leave `AMB_Layer2_Canonical_v7_0.md` **out** of the Project for now — it's large, and
   you'll pull exact wording from it only when you specifically need it (see Method 2).

**Using it (every time):**
- Start a chat inside that Project and just ask for what you need, e.g. *"Draft a
  developer-facing explainer of how Apple Pay messages work in AMB,"* or *"Turn the List
  Picker requirements into a one-page brief."* Because the map and structures are in the
  Project, Claude can work accurately without you pasting anything.
- When you need Apple's **exact words** (for a quote, a legal line, a precise field
  description), use Method 2 to fetch that one section and paste it into the chat.

> If the Project won't hold all the compact files at once, prioritise
> `AMB_Schemas_Reference.md` and `conformance_checklist.md`. Claude-product storage limits
> change over time; if you hit one, ask Claude "what are the current Project knowledge
> limits?" or check support.claude.com.

### Method 2 — Fetching one exact section (a light, occasional skill)

The canonical is ~13,500 lines. You never need all of it — you need the *right slice*.
The index exists to find that slice.

The no-tools way that always works:
1. Open `AMB_Schemas_Reference.md` (or `amb_index.json`) and find your topic — say
   "ListPickerMessage." Next to it you'll see something like `canonical L2015–2018`.
2. Open `AMB_Layer2_Canonical_v7_0.md` in any text editor, go to those line numbers, and
   copy just that block.
3. Paste that block into your chat. That's the exact, citable Apple text for that topic,
   at a size that fits.

That's the whole discipline: **look up the line numbers, copy that span, use that.** Never
paste the whole file.

### Method 3 — Developer / automation uses (hand this to a developer)

These are real and valuable, but they are engineering tasks. If you don't do this kind of
work, this is the section you forward to a developer (or ask Claude Code to do — see §6):

- **Validating real messages:** point code at `schemas/` to automatically check that
  outgoing/incoming AMB messages are correctly formed.
- **Generating client code / a mock server:** feed `amb.openapi.json` to standard OpenAPI
  tooling.
- **Contract tests:** run the `fixtures/` against the schemas in a test suite so a future
  canonical change that breaks something gets caught automatically.
- **Feeding an AI system (RAG):** use `amb_index.json` as the chunking map and the schemas
  as grounding, so an assistant answers AMB questions with citations.

You don't need to understand these to own the kit. They're what the kit *enables* for a
technical teammate.

---

## 6. Keeping it updated (when Apple changes something)

You only do this when the underlying Apple documentation actually changes — which is
infrequent. The update itself is **one command**, but running it needs either a little
command-line comfort or a tool to run it for you. Both paths below produce the same result.

**What you do first (either path):** open `AMB_Layer2_Canonical_v7_0.md`, make your edit to
reflect Apple's change, save.

**Path A — let Claude do it for you (recommended for your situation).**
Use **Claude Code** or **Claude Cowork** (the tools that can work with files on your
computer). Open the `amb-kit` folder with it and say:
> "Run `build_all.py` in this folder and tell me if every step validated."
It will run the command, and because the pipeline **aborts on any error**, "it finished
cleanly" means everything regenerated correctly. Then it can tell you what changed.

**Path B — do it yourself in the Terminal (if you're comfortable).**
```bash
# one-time setup:
pip install jsonschema openapi-spec-validator

# each time you've edited the canonical:
cd path/to/amb-kit
python3 build_all.py
```
If it prints a SUMMARY at the end with no "ABORT," you're done. If it aborts, it will name
the step that failed — send that message to Claude and it'll help you fix it. A broken file
is never produced; the run stops instead.

**After updating (either path):** re-upload the refreshed compact files to your Claude
Project (Method 1) so your content work uses the new version.

> **You do not maintain any of the generated files by hand — ever.** If you find yourself
> editing a schema or the index directly, stop: that edit will be erased the next time the
> pipeline runs. Put the change in the canonical instead, and regenerate.

---

## 7. Cheat sheet — which file answers which question

- *"What fields does this message type have?"* → `AMB_Schemas_Reference.md` (read) or
  `schemas/` (for tools).
- *"Is this feature required for Apple to approve us?"* → `conformance_checklist.md`.
- *"Apple didn't say how to handle X — what do we do?"* → `decision_records/`.
- *"What are Apple's exact words on X?"* → find the line numbers in the reference/index,
  copy that span from the canonical.
- *"What endpoints do we call?"* → `amb.openapi.json` (or the index's endpoints list).
- *"Where might Apple's docs be unclear or self-contradictory?"* → `schema_coverage_report.md`
  and the conflict register inside `amb_index.json`.
- *"What are the legal/privacy terms?"* → the canonical's Part 4, plus the `service-terms`,
  `apple-business-register-tou`, and `amb-privacy` entries in the index's provenance.

---

## 8. Small glossary

- **Canonical** — the master document; your single source of truth.
- **Schema** — a precise definition of a data structure (which fields exist, their types,
  which are required). Lets tools check a message is built correctly.
- **Index** — a map into the canonical (topics → exact line numbers), so you fetch a slice
  instead of the whole thing.
- **OpenAPI** — a standard file format describing web endpoints, used to generate code and
  test tools.
- **Fixtures** — real example messages, used to test that the schemas match reality.
- **Provenance** — the record of where each fact came from and how current it is.
- **Regenerate / build** — running `build_all.py` to refresh all generated files from the
  canonical.
- **Project (Claude)** — a workspace that keeps a set of files available to every chat
  inside it, so you don't re-upload.

---

## 9. What not to do (the short list)

1. Don't keep old loose copies of these files next to the folder (see §2).
2. Don't edit any generated file by hand — edit the canonical and regenerate.
3. Don't paste the whole canonical into a chat — fetch the relevant span (Method 2).
4. Don't treat the legal/privacy layer or anything marked "verify" as settled without
   checking Apple's current source; the coverage report and provenance notes tell you
   what still needs a human's eye.

---

*If any step here is unclear, paste this file (or the relevant section) into a Claude chat
and ask it to walk you through that part for your specific setup — that's a perfectly good
way to use it.*
