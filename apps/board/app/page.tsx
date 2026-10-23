import Link from "next/link";
import { listBrands, STAGES } from "@/lib/db";

export const dynamic = "force-dynamic";

// Stage accents (dot colors), mirroring the Strategic Accounts board feel.
const ACCENT: Record<string, string> = {
  brand_approval: "#8a929c",
  ux_approval: "#2f6db0",
  experience_review: "#d98a1f",
  launch: "#1f8b5b",
};

export default async function Home() {
  const brands = await listBrands();
  // Each brand sits in one column = its current stage (null → the first stage).
  const byStage: Record<string, typeof brands> = {};
  for (const s of STAGES) byStage[s.key] = [];
  for (const b of brands) {
    const key = b.stage && byStage[b.stage] ? b.stage : STAGES[0].key;
    byStage[key].push(b);
  }

  return (
    <main>
      <div style={{ marginBottom: 18 }}>
        <h1 style={{ fontSize: 24, fontWeight: 800, color: "#16375c", margin: 0 }}>AMB Approval</h1>
        <p style={{ color: "#6b7280", marginTop: 4, fontSize: 13 }}>
          {brands.length} brand{brands.length === 1 ? "" : "s"} · Apple Messages for Business pipeline
        </p>
      </div>

      <div style={{ display: "flex", gap: 14, alignItems: "flex-start", overflowX: "auto", paddingBottom: 12 }}>
        {STAGES.map((s) => {
          const cards = byStage[s.key];
          return (
            <div key={s.key} style={{ width: 270, flex: "0 0 270px", background: "rgba(0,0,0,0.025)", border: "1px solid #e8ebef", borderRadius: 12 }}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "11px 14px", borderBottom: "1px solid #e8ebef" }}>
                <span style={{ display: "flex", alignItems: "center", gap: 8, fontSize: 13, fontWeight: 600, color: "#374151" }}>
                  <span style={{ width: 9, height: 9, borderRadius: 9, background: ACCENT[s.key] }} />
                  {s.label}
                </span>
                <span style={{ fontSize: 11, fontFamily: "ui-monospace,monospace", color: "#9aa4b1" }}>{cards.length}</span>
              </div>
              <div style={{ padding: 10, display: "flex", flexDirection: "column", gap: 10, minHeight: 60 }}>
                {cards.length === 0 && <p style={{ fontSize: 11, color: "#c3cad3", textAlign: "center", padding: "14px 0" }}>—</p>}
                {cards.map((b) => {
                  const artCount = Object.values(b.artifactsByStage).reduce((n, a) => n + a.length, 0);
                  return (
                    <Link key={b.name} href={`/brand/${b.name}`} style={{ textDecoration: "none" }}>
                      <div style={{ background: "#fff", border: "1px solid #e3e7ec", borderRadius: 10, padding: "12px 13px", boxShadow: "0 1px 2px rgba(0,0,0,.04)" }}>
                        <div style={{ fontSize: 14, fontWeight: 700, color: "#16375c" }}>{b.name}</div>
                        {artCount > 0 && (
                          <div style={{ fontSize: 11, color: "#9aa4b1", marginTop: 2 }}>{artCount} artifact{artCount === 1 ? "" : "s"}</div>
                        )}
                        <div style={{ marginTop: 10 }}>
                          <span style={{ fontSize: 11, color: b.owner ? "#55606e" : "#b0b8c1", background: "rgba(0,0,0,0.04)", border: "1px solid #e8ebef", borderRadius: 5, padding: "2px 7px" }}>
                            {b.owner || "Unclaimed"}
                          </span>
                        </div>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
      <p style={{ marginTop: 10, fontSize: 12, color: "#9aa4b1" }}>
        Click a tile to open the brand · state in Supabase · artifacts in Slack · runs via <code>/amb</code>.
      </p>
    </main>
  );
}
