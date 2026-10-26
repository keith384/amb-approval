import Link from "next/link";
import { notFound } from "next/navigation";
import { getBrand, listUsers, STAGES } from "@/lib/db";
import { moveStage, setOwner } from "@/app/actions";

export const dynamic = "force-dynamic";

const ACCENT: Record<string, string> = {
  brand_approval: "#8a929c", ux_approval: "#2f6db0", experience_review: "#d98a1f", launch: "#1f8b5b",
};
const KIND_LABEL: Record<string, string> = {
  doc: "Brand doc", usecases_form: "Use Cases form", readiness_form: "Readiness form",
  readiness_note: "Readiness note", scope: "Scope", storyboard: "Storyboard", shotlist: "Shot list",
  review: "Review", timestamp_index: "Timestamp index", artifact: "File",
};

const card: React.CSSProperties = { background: "#fff", border: "1px solid #e3e7ec", borderRadius: 12, boxShadow: "0 1px 2px rgba(0,0,0,.04)" };
const btn: React.CSSProperties = { padding: "6px 12px", borderRadius: 8, border: "1px solid #c9d2dc", background: "#fff", cursor: "pointer", fontSize: 13 };

export default async function BrandPage({ params }: { params: Promise<{ brand: string }> }) {
  const { brand } = await params;
  const b = await getBrand(brand);
  if (!b) notFound();
  const users = await listUsers();
  const stageLabel = STAGES.find((s) => s.key === b.stage)?.label ?? "Not started";

  async function ownerAction(formData: FormData) {
    "use server";
    await setOwner(brand, String(formData.get("owner") || ""));
  }

  return (
    <main style={{ maxWidth: 1040, margin: "0 auto" }}>
      <Link href="/" style={{ color: "#6b7280", textDecoration: "none", fontSize: 13 }}>← Board</Link>
      <div style={{ display: "flex", alignItems: "center", gap: 12, margin: "10px 0 20px" }}>
        <h1 style={{ fontSize: 26, fontWeight: 800, color: "#16375c", margin: 0 }}>{b.name}</h1>
        <span style={{ display: "inline-flex", alignItems: "center", gap: 6, fontSize: 12, fontWeight: 600, color: "#374151", background: "rgba(0,0,0,0.04)", border: "1px solid #e8ebef", borderRadius: 20, padding: "3px 11px" }}>
          <span style={{ width: 8, height: 8, borderRadius: 8, background: ACCENT[b.stage ?? ""] ?? "#c3cad3" }} />
          {stageLabel}
        </span>
        <span style={{ fontSize: 13, color: "#9aa4b1", marginLeft: "auto" }}>Owner: <b style={{ color: b.owner ? "#374151" : "#c3cad3" }}>{b.owner ?? "unassigned"}</b></span>
      </div>

      {/* Stage cards */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(230px,1fr))", gap: 14 }}>
        {STAGES.map((s) => {
          const arts = b.artifactsByStage[s.key] ?? [];
          return (
            <div key={s.key} style={{ ...card, padding: 15 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 7, marginBottom: 10 }}>
                <span style={{ width: 8, height: 8, borderRadius: 8, background: ACCENT[s.key] }} />
                <span style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700 }}>{s.label}</span>
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 7 }}>
                {arts.length === 0 && <span style={{ color: "#c3cad3", fontSize: 12.5 }}>—</span>}
                {arts.map((a, i) => {
                  const inner = (
                    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 8, padding: "7px 9px", borderRadius: 8, border: "1px solid #eef1f4", background: "#fafbfc" }}>
                      <span style={{ fontSize: 12, color: "#374151", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                        {KIND_LABEL[a.kind ?? ""] ?? a.label}
                      </span>
                      {a.link && <span style={{ fontSize: 12, color: "#2f6db0" }}>↗</span>}
                    </div>
                  );
                  return a.link
                    ? <a key={i} href={a.link} target="_blank" style={{ textDecoration: "none" }}>{inner}</a>
                    : <div key={i} title="Generated locally — run via Slack to get a link">{inner}</div>;
                })}
              </div>
            </div>
          );
        })}
      </div>

      {/* Controls */}
      <div style={{ ...card, padding: 16, marginTop: 18, display: "flex", gap: 28, flexWrap: "wrap", alignItems: "flex-start" }}>
        <div>
          <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700, marginBottom: 7 }}>Move stage</div>
          <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
            {STAGES.map((s) => (
              <form key={s.key} action={moveStage.bind(null, b.name, s.key)}>
                <button style={{ ...btn, background: b.stage === s.key ? "#16375c" : "#fff", color: b.stage === s.key ? "#fff" : "#1b2430", borderColor: b.stage === s.key ? "#16375c" : "#c9d2dc" }}>{s.label}</button>
              </form>
            ))}
          </div>
        </div>
        <div>
          <div style={{ fontSize: 11, textTransform: "uppercase", letterSpacing: ".06em", color: "#9aa4b1", fontWeight: 700, marginBottom: 7 }}>Next-step owner</div>
          <form action={ownerAction} style={{ display: "flex", gap: 6 }}>
            <select name="owner" defaultValue={b.owner ?? ""} style={{ padding: "6px 10px", border: "1px solid #c9d2dc", borderRadius: 8, fontSize: 13, minWidth: 170 }}>
              <option value="">— unassigned —</option>
              {b.owner && !users.some((u) => u.name === b.owner) && <option value={b.owner}>{b.owner}</option>}
              {users.map((u) => <option key={u.name} value={u.name}>{u.name}</option>)}
            </select>
            <button style={btn}>Save</button>
          </form>
        </div>
      </div>

      <p style={{ marginTop: 14, fontSize: 12.5, color: "#9aa4b1" }}>
        Generate or update artifacts by mentioning <b>@AMB Approval</b> (or <code>/amb</code>) in Slack — they post to the thread and link here.
      </p>

      {/* History */}
      <h2 style={{ fontSize: 13, color: "#16375c", marginTop: 22, marginBottom: 8 }}>History</h2>
      <div style={{ ...card, padding: 14, fontSize: 12.5 }}>
        {b.events.length === 0 && <span style={{ color: "#c3cad3" }}>no events yet</span>}
        {b.events.map((e, i) => (
          <div key={i} style={{ padding: "4px 0", color: "#55606e", borderBottom: i < b.events.length - 1 ? "1px solid #f1f3f5" : undefined }}>
            <span style={{ fontFamily: "ui-monospace,monospace", color: "#9aa4b1" }}>{(e.at || "").slice(0, 16).replace("T", " ")}</span>
            {"  ·  "}<b>{e.action}</b>{e.detail ? ` — ${e.detail}` : ""}
          </div>
        ))}
      </div>
    </main>
  );
}
