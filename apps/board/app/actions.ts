"use server";

import { revalidatePath } from "next/cache";
import * as db from "@/lib/db";

// Board = tracking + stage/owner edits. Tool RUNS happen on the Mac via `/amb` in
// Slack (Apple Vision, multi-minute); the board only reads/updates pipeline state.
export async function moveStage(brand: string, stage: string) {
  await db.moveStage(brand, stage);
  revalidatePath(`/brand/${brand}`);
  revalidatePath("/");
}

export async function setOwner(brand: string, owner: string) {
  await db.setOwner(brand, owner);
  revalidatePath(`/brand/${brand}`);
  revalidatePath("/");
}
