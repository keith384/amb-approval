import fs from "fs";
import path from "path";

// The board reads the same brand folders the Slack bot + worker write to.
const REPO = path.resolve(process.cwd(), "../..");
export const BRANDS_DIR = path.join(REPO, "brands");

export const STAGES = [
  { key: "brand_approval", label: "Brand Approval", tool: "brand-doc" },
  { key: "ux_approval", label: "UX Approval", tool: "storyboard" },
  { key: "experience_review", label: "Experience Review", tool: "review" },
  { key: "launch", label: "Launch", tool: null },
] as const;

export type StageKey = (typeof STAGES)[number]["key"];

// Which output files belong to which stage (by filename pattern).
const STAGE_FILES: Record<StageKey, RegExp> = {
  brand_approval: /^(brand-approval-.*\.html|.*-usecases\.pdf|.*-readiness\.pdf|readiness-.*\.md|scope\.json)$/,
  ux_approval: /^(storyboard-.*\.html|shotlist-.*\.json)$/,
  experience_review: /^(review-.*|timestamp-index-.*|review\.json)/,
  launch: /^launch/,
};

export interface BrandEvent { at: string; action: string; detail?: string }
export interface BrandRow {
  name: string;
  stage: string | null;
  events: BrandEvent[];
  lastAt: string | null;
  artifactsByStage: Record<string, string[]>;
  owner: string | null;
}

function readState(dir: string): { stage: string | null; events: BrandEvent[]; owner?: string } {
  const f = path.join(dir, "state.json");
  if (!fs.existsSync(f)) return { stage: null, events: [] };
  try { return JSON.parse(fs.readFileSync(f, "utf8")); } catch { return { stage: null, events: [] }; }
}

function listOutputs(dir: string): string[] {
  const out = path.join(dir, "output");
  if (!fs.existsSync(out)) return [];
  const files: string[] = [];
  for (const e of fs.readdirSync(out, { withFileTypes: true })) {
    if (e.isDirectory()) {
      for (const f of fs.readdirSync(path.join(out, e.name))) files.push(`${e.name}/${f}`);
    } else files.push(e.name);
  }
  return files;
}

function bucket(files: string[]): Record<string, string[]> {
  const by: Record<string, string[]> = {};
  for (const s of STAGES) by[s.key] = [];
  for (const f of files) {
    const base = f.split("/").pop()!;
    for (const s of STAGES) {
      if (STAGE_FILES[s.key].test(base) || STAGE_FILES[s.key].test(f)) { by[s.key].push(f); break; }
    }
  }
  return by;
}

export function listBrands(): BrandRow[] {
  if (!fs.existsSync(BRANDS_DIR)) return [];
  const rows: BrandRow[] = [];
  for (const e of fs.readdirSync(BRANDS_DIR, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    const dir = path.join(BRANDS_DIR, e.name);
    const st = readState(dir);
    const files = listOutputs(dir);
    rows.push({
      name: e.name, stage: st.stage, events: st.events ?? [],
      lastAt: st.events?.length ? st.events[st.events.length - 1].at : null,
      artifactsByStage: bucket(files), owner: st.owner ?? null,
    });
  }
  return rows.sort((a, b) => a.name.localeCompare(b.name));
}

export function getBrand(name: string): BrandRow | null {
  return listBrands().find((b) => b.name === name) ?? null;
}

export function readArtifact(brand: string, file: string): { body: Buffer; type: string } | null {
  const safe = path.normalize(file).replace(/^(\.\.(\/|\\|$))+/, "");
  const p = path.join(BRANDS_DIR, brand, "output", safe);
  if (!p.startsWith(path.join(BRANDS_DIR, brand))) return null;
  if (!fs.existsSync(p)) return null;
  const ext = path.extname(p).toLowerCase();
  const type = ext === ".html" ? "text/html" : ext === ".pdf" ? "application/pdf"
    : ext === ".json" ? "application/json" : "text/plain; charset=utf-8";
  return { body: fs.readFileSync(p), type };
}
