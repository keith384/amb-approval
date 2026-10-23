import { createClient } from "@/lib/supabase/server";
import { redirect } from "next/navigation";

export const dynamic = "force-dynamic";

const ERRORS: Record<string, string> = {
  domain: "Use your @linqapp.com Google account.",
  oauth_failed: "Google sign-in could not start. Try again.",
  auth_failed: "Sign-in failed. Try again.",
};

export default async function LoginPage({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (user) redirect("/");
  const { error } = await searchParams;

  return (
    <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", background: "#e6e8ed" }}>
      <div style={{ background: "#fff", boxShadow: "0 1px 3px rgba(0,0,0,.08)", borderRadius: 14, border: "1px solid rgba(0,0,0,0.06)", padding: 40, width: "100%", maxWidth: 360, display: "flex", flexDirection: "column", alignItems: "center", gap: 22 }}>
        <div style={{ textAlign: "center" }}>
          <p style={{ fontWeight: 800, fontSize: 24, color: "#16375c", margin: 0 }}>AMB Approval</p>
          <p style={{ fontSize: 10, fontFamily: "ui-monospace,monospace", letterSpacing: ".15em", textTransform: "uppercase", marginTop: 6, color: "rgba(0,0,0,0.4)" }}>
            Apple Messages for Business
          </p>
        </div>
        {error && <p style={{ fontSize: 12.5, color: "#b42318", margin: 0, textAlign: "center" }}>{ERRORS[error] ?? "Sign-in error."}</p>}
        <form action="/api/auth/login" method="POST" style={{ width: "100%" }}>
          <button type="submit" style={{ width: "100%", display: "flex", alignItems: "center", justifyContent: "center", gap: 12, border: "1px solid rgba(0,0,0,0.15)", borderRadius: 10, padding: "10px 16px", fontSize: 14, fontWeight: 500, background: "#fff", cursor: "pointer" }}>
            <svg width="18" height="18" viewBox="0 0 24 24">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05" />
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
            </svg>
            Sign in with Google
          </button>
        </form>
        <p style={{ fontSize: 11, color: "rgba(0,0,0,0.4)", margin: 0 }}>Linq internal · @linqapp.com only</p>
      </div>
    </div>
  );
}
