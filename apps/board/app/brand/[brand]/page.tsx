import Link from "next/link";
import { notFound } from "next/navigation";
import { getBrand, STAGES } from "@/lib/brands";
import { triggerTool, moveStage, setOwner } from "@/app/actions";

export const dynamic = "force-dynamic";

const btn = { padding: "6px 12px", borderRadius: 7, border: "1px solid #c9d2dc", background: "#fff", cursor: "pointer", fontSize: 13 } as const;

export default async function BrandPage({ params }: { params: Promise<{ brand: string }> }) {
  const { brand } = await params;
  const b = getBrand(brand);
  if (!b) notFound();

  async function ownerAction(formData: FormData) {
    "use server";
    await setOwner(brand, String(formData.get("owner") || ""));
  }

  return (
    <main>
      <Link href="/" style={{ color: "#6b7280", textDecoration: "none", fontSize: 13 }}>← Board</Link>
      <h1 style={{ fontSize: 24, fontWeight: 800, color: "#16375c", margin: "8px 0 2px" }}>{b.name}</h1>
      <div style={{ color: "#6b7280", marginBottom: 18 }}>
        stage: <b>{b.stage ?? "not started"}</b> · owner: {b.owner ?? "—"}
      </div>

      {/* Stage cards */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(250px,1fr))", gap: 14 }}>
        {STAGES.map((s) => {
          const arts = b.artifactsByStage[s.key] ?? [];
          return (
            <div key={s.key} style={{ background: "#fff", border: "1px solid #e3e7ec", borderRadius: 10, padding: 14 }}>
              <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700 }}>{s.label}</div>
              <div style={{ margin: "8px 0" }}>
                {arts.length === 0 && <span style={{ color: "#b0b8c1", fontSize: 13 }}>no artifacts</span>}
                {arts.map((f) => (
                  <div key={f}><a href={`/artifact/${b.name}/${encodeURIComponent(f)}`} target="_blank" style={{ color: "#2f6db0", fontSize: 12.5, textDecoration: "none" }}>{f}</a></div>
                ))}
              </div>
              {s.tool && (
                <form action={triggerTool.bind(null, b.name, s.tool)}>
                  <button style={btn}>Run {s.tool}</button>
                </form>
              )}
            </div>
          );
        })}
      </div>

      {/* Controls */}
      <div style={{ display: "flex", gap: 24, marginTop: 22, flexWrap: "wrap", alignItems: "flex-start" }}>
        <div>
          <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700, marginBottom: 6 }}>Move stage</div>
          <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
            {STAGES.map((s) => (
              <form key={s.key} action={moveStage.bind(null, b.name, s.key)}>
                <button style={{ ...btn, background: b.stage === s.key ? "#16375c" : "#fff", color: b.stage === s.key ? "#fff" : "#1b2430" }}>{s.label}</button>
              </form>
            ))}
          </div>
        </div>
        <div>
          <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700, marginBottom: 6 }}>Next-step owner</div>
          <form action={ownerAction} style={{ display: "flex", gap: 6 }}>
            <input name="owner" defaultValue={b.owner ?? ""} placeholder="name" style={{ padding: "6px 10px", border: "1px solid #c9d2dc", borderRadius: 7, fontSize: 13 }} />
            <button style={btn}>Save</button>
          </form>
        </div>
      </div>

      {/* Upload hint — real upload goes to blob in the Vercel build */}
      <div style={{ marginTop: 20, fontSize: 12.5, color: "#6b7280" }}>
        To run an Experience Review, drop the recording in <code>brands/{b.name}/inputs/</code> then Run review.
        (Production: drag-to-upload → blob → worker.)
      </div>

      {/* History */}
      <h2 style={{ fontSize: 13, color: "#16375c", marginTop: 24 }}>History</h2>
      <div style={{ background: "#fff", border: "1px solid #e3e7ec", borderRadius: 10, padding: 12, fontSize: 12.5 }}>
        {b.events.length === 0 && <span style={{ color: "#b0b8c1" }}>no events yet</span>}
        {[...b.events].reverse().map((e, i) => (
          <div key={i} style={{ padding: "3px 0", color: "#55606e" }}>
            <span style={{ fontFamily: "ui-monospace,monospace", color: "#9aa4b1" }}>{e.at.slice(0, 16).replace("T", " ")}</span>
            {" · "}<b>{e.action}</b>{e.detail ? ` — ${e.detail}` : ""}
          </div>
        ))}
      </div>
    </main>
  );
}
