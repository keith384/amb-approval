import Link from "next/link";
import { listBrands, STAGES } from "@/lib/db";

export const dynamic = "force-dynamic";

const STATE_COLOR: Record<string, string> = { done: "#1f8b5b", active: "#2f6db0", none: "#c3cad3" };

function cellState(stageKey: string, brandStage: string | null, count: number): "done" | "active" | "none" {
  const order: string[] = STAGES.map((s) => s.key);
  const bi = brandStage ? order.indexOf(brandStage) : -1;
  const si = order.indexOf(stageKey);
  if (count) return "done";
  if (bi >= 0 && si <= bi) return "active";
  return "none";
}

export default async function Home() {
  const brands = await listBrands();
  return (
    <main>
      <h1 style={{ fontSize: 24, fontWeight: 800, color: "#16375c", margin: 0 }}>AMB Approval Board</h1>
      <p style={{ color: "#6b7280", marginTop: 4 }}>
        Apple Messages for Business pipeline · {brands.length} brand{brands.length === 1 ? "" : "s"} · tracking (artifacts live in Slack)
      </p>

      <div style={{ marginTop: 20, overflowX: "auto" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13, background: "#fff", borderRadius: 10, overflow: "hidden", boxShadow: "0 1px 3px rgba(0,0,0,.06)" }}>
          <thead>
            <tr style={{ background: "#16375c", color: "#fff", textAlign: "left" }}>
              <th style={{ padding: "10px 14px" }}>Brand</th>
              {STAGES.map((s) => <th key={s.key} style={{ padding: "10px 14px" }}>{s.label}</th>)}
              <th style={{ padding: "10px 14px" }}>Owner</th>
            </tr>
          </thead>
          <tbody>
            {brands.length === 0 && (
              <tr><td colSpan={STAGES.length + 2} style={{ padding: 18, color: "#9aa4b1" }}>
                No brands yet. Run <code>/amb brand-doc &lt;brand&gt;</code> in Slack — it records the brand here.
              </td></tr>
            )}
            {brands.map((b) => (
              <tr key={b.name} style={{ borderTop: "1px solid #eef1f4" }}>
                <td style={{ padding: "10px 14px", fontWeight: 600 }}>
                  <Link href={`/brand/${b.name}`} style={{ color: "#16375c", textDecoration: "none" }}>{b.name}</Link>
                </td>
                {STAGES.map((s) => {
                  const n = (b.artifactsByStage[s.key] ?? []).length;
                  const state = cellState(s.key, b.stage, n);
                  return (
                    <td key={s.key} style={{ padding: "10px 14px" }}>
                      <Link href={`/brand/${b.name}`} style={{ textDecoration: "none", color: "inherit", display: "flex", alignItems: "center", gap: 7 }}>
                        <span style={{ width: 9, height: 9, borderRadius: 9, background: STATE_COLOR[state], display: "inline-block" }} />
                        <span style={{ color: state === "none" ? "#b0b8c1" : "#374151" }}>
                          {n ? `${n} artifact${n === 1 ? "" : "s"}` : state === "active" ? "in progress" : "—"}
                        </span>
                      </Link>
                    </td>
                  );
                })}
                <td style={{ padding: "10px 14px", color: "#6b7280" }}>{b.owner ?? "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p style={{ marginTop: 14, fontSize: 12, color: "#9aa4b1" }}>
        State in Supabase · artifacts in Slack · tool runs via <code>/amb</code> in #amb-implimenation.
      </p>
    </main>
  );
}
