import Link from "next/link";
import { notFound } from "next/navigation";
import { getBrand, listUsers, STAGES } from "@/lib/db";
import { moveStage, setOwner } from "@/app/actions";

export const dynamic = "force-dynamic";

const btn = { padding: "6px 12px", borderRadius: 7, border: "1px solid #c9d2dc", background: "#fff", cursor: "pointer", fontSize: 13 } as const;

export default async function BrandPage({ params }: { params: Promise<{ brand: string }> }) {
  const { brand } = await params;
  const b = await getBrand(brand);
  if (!b) notFound();
  const users = await listUsers();

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

      {/* Stage cards — artifacts link to Slack */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(250px,1fr))", gap: 14 }}>
        {STAGES.map((s) => {
          const arts = b.artifactsByStage[s.key] ?? [];
          return (
            <div key={s.key} style={{ background: "#fff", border: "1px solid #e3e7ec", borderRadius: 10, padding: 14 }}>
              <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700 }}>{s.label}</div>
              <div style={{ margin: "8px 0 2px" }}>
                {arts.length === 0 && <span style={{ color: "#b0b8c1", fontSize: 13 }}>no artifacts</span>}
                {arts.map((a, i) => (
                  <div key={i}>
                    {a.link
                      ? <a href={a.link} target="_blank" style={{ color: "#2f6db0", fontSize: 12.5, textDecoration: "none" }}>{a.label || a.kind} ↗</a>
                      : <span style={{ fontSize: 12.5, color: "#55606e" }}>{a.label || a.kind}</span>}
                  </div>
                ))}
              </div>
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
            <select name="owner" defaultValue={b.owner ?? ""} style={{ padding: "6px 10px", border: "1px solid #c9d2dc", borderRadius: 7, fontSize: 13, minWidth: 160 }}>
              <option value="">— unassigned —</option>
              {b.owner && !users.some((u) => u.name === b.owner) && <option value={b.owner}>{b.owner}</option>}
              {users.map((u) => <option key={u.name} value={u.name}>{u.name}</option>)}
            </select>
            <button style={btn}>Save</button>
          </form>
        </div>
      </div>

      <div style={{ marginTop: 20, fontSize: 12.5, color: "#6b7280" }}>
        Generate artifacts with <code>/amb brand-doc | storyboard | review {b.name}</code> in Slack — they post to the thread and appear here as links.
      </div>

      {/* History */}
      <h2 style={{ fontSize: 13, color: "#16375c", marginTop: 24 }}>History</h2>
      <div style={{ background: "#fff", border: "1px solid #e3e7ec", borderRadius: 10, padding: 12, fontSize: 12.5 }}>
        {b.events.length === 0 && <span style={{ color: "#b0b8c1" }}>no events yet</span>}
        {b.events.map((e, i) => (
          <div key={i} style={{ padding: "3px 0", color: "#55606e" }}>
            <span style={{ fontFamily: "ui-monospace,monospace", color: "#9aa4b1" }}>{(e.at || "").slice(0, 16).replace("T", " ")}</span>
            {" · "}<b>{e.action}</b>{e.detail ? ` — ${e.detail}` : ""}
          </div>
        ))}
      </div>
    </main>
  );
}
