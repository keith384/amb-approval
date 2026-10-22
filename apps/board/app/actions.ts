"use server";

import { spawn } from "child_process";
import fs from "fs";
import path from "path";
import { revalidatePath } from "next/cache";
import { BRANDS_DIR } from "@/lib/brands";

const REPO = path.resolve(process.cwd(), "../..");

// Kick a tool via the same dispatcher the Slack bot uses. Long tools (review) run
// detached; the board reflects the new state/artifacts on the next refresh.
export async function triggerTool(brand: string, sub: string) {
  const child = spawn("python3", [path.join(REPO, "apps/slack-bot/amb.py"), sub, brand], {
    cwd: REPO, detached: true, stdio: "ignore",
    env: { ...process.env },
  });
  child.unref();
  revalidatePath(`/brand/${brand}`);
  revalidatePath("/");
}

export async function moveStage(brand: string, stage: string) {
  const f = path.join(BRANDS_DIR, brand, "state.json");
  const st = fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, "utf8")) : { stage: null, events: [] };
  st.stage = stage;
  st.events = st.events ?? [];
  st.events.push({ at: new Date().toISOString(), action: "stage_moved", detail: stage });
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, JSON.stringify(st, null, 2));
  syncHubspot(brand);
  revalidatePath(`/brand/${brand}`);
  revalidatePath("/");
}

// One-way board → HubSpot on stage change. Dry-run unless AMB_HUBSPOT_WRITE is set
// (and the brand is mapped to a deal + the 4 custom properties exist).
function syncHubspot(brand: string) {
  try {
    const args = [path.join(REPO, "apps/slack-bot/hubspot_sync.py"), "sync", brand];
    if (process.env.AMB_HUBSPOT_WRITE) args.push("--write");
    spawn("python3", args, { cwd: REPO, detached: true, stdio: "ignore", env: { ...process.env } }).unref();
  } catch { /* best-effort; board stays source of record */ }
}

export async function setOwner(brand: string, owner: string) {
  const f = path.join(BRANDS_DIR, brand, "state.json");
  const st = fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, "utf8")) : { stage: null, events: [] };
  st.owner = owner;
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, JSON.stringify(st, null, 2));
  revalidatePath(`/brand/${brand}`);
  revalidatePath("/");
}
