import { createClient } from "@supabase/supabase-js";

// Shared Supabase project — pipeline STATE lives here; artifacts live in Slack
// (amb_artifact.link). Board reads/writes server-side with the service role.
// Accept either our var or the ones the Vercel↔Supabase integration injects.
const URL = (process.env.NEXT_PUBLIC_SUPABASE_URL || process.env.SUPABASE_URL)!;
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY!;
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function sb(): any {
  return createClient(URL, KEY, { auth: { persistSession: false } });
}

export const STAGES = [
  { key: "brand_approval", label: "Brand Approval" },
  { key: "ux_approval", label: "UX Approval" },
  { key: "experience_review", label: "Experience Review" },
  { key: "launch", label: "Launch" },
] as const;

export interface BrandEvent { at: string; action: string; detail?: string | null }
export interface Artifact { stage: string | null; kind: string | null; label: string | null; link: string | null }
export interface BrandRow {
  name: string;
  stage: string | null;
  owner: string | null;
  lastAt: string | null;
  events: BrandEvent[];
  artifactsByStage: Record<string, Artifact[]>;
}

function bucket(arts: Artifact[]): Record<string, Artifact[]> {
  const by: Record<string, Artifact[]> = {};
  for (const s of STAGES) by[s.key] = [];
  for (const a of arts) if (a.stage && by[a.stage]) by[a.stage].push(a);
  return by;
}

export async function listBrands(): Promise<BrandRow[]> {
  const supabase = sb();
  const [{ data: brands }, { data: arts }, { data: events }] = await Promise.all([
    supabase.from("amb_brand").select("name, stage, owner, updated_at").order("name"),
    supabase.from("amb_artifact").select("brand, stage, kind, label, link"),
    supabase.from("amb_event").select("brand, action, detail, at").order("at", { ascending: false }),
  ]);
  const artsByBrand: Record<string, Artifact[]> = {};
  for (const a of arts ?? []) (artsByBrand[a.brand] ??= []).push(a);
  const lastByBrand: Record<string, string> = {};
  for (const e of events ?? []) if (!lastByBrand[e.brand]) lastByBrand[e.brand] = e.at;
  return (brands ?? []).map((b: { name: string; stage: string | null; owner: string | null }) => ({
    name: b.name, stage: b.stage, owner: b.owner,
    lastAt: lastByBrand[b.name] ?? null, events: [],
    artifactsByStage: bucket(artsByBrand[b.name] ?? []),
  }));
}

export async function getBrand(name: string): Promise<BrandRow | null> {
  const supabase = sb();
  const { data: b } = await supabase.from("amb_brand").select("name, stage, owner").eq("name", name).maybeSingle();
  if (!b) return null;
  const [{ data: arts }, { data: events }] = await Promise.all([
    supabase.from("amb_artifact").select("brand, stage, kind, label, link").eq("brand", name),
    supabase.from("amb_event").select("action, detail, at").eq("brand", name).order("at", { ascending: false }),
  ]);
  return {
    name: b.name, stage: b.stage, owner: b.owner,
    lastAt: events?.[0]?.at ?? null, events: (events ?? []) as BrandEvent[],
    artifactsByStage: bucket((arts ?? []) as Artifact[]),
  };
}

export async function moveStage(name: string, stage: string): Promise<void> {
  const supabase = sb();
  const now = new Date().toISOString();
  await supabase.from("amb_brand").upsert(
    { name, stage, stage_entered_at: now, updated_at: now }, { onConflict: "name" });
  await supabase.from("amb_event").insert({ brand: name, action: "stage_moved", detail: stage });
}

export async function setOwner(name: string, owner: string): Promise<void> {
  const supabase = sb();
  await supabase.from("amb_brand").upsert(
    { name, owner, updated_at: new Date().toISOString() }, { onConflict: "name" });
  await supabase.from("amb_event").insert({ brand: name, action: "owner_set", detail: owner });
}
