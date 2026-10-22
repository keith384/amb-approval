import { readArtifact } from "@/lib/brands";

export const dynamic = "force-dynamic";

export async function GET(_req: Request, ctx: { params: Promise<{ brand: string; file: string }> }) {
  const { brand, file } = await ctx.params;
  const art = readArtifact(brand, decodeURIComponent(file));
  if (!art) return new Response("Not found", { status: 404 });
  return new Response(new Uint8Array(art.body), {
    headers: { "Content-Type": art.type, "Cache-Control": "no-store" },
  });
}
