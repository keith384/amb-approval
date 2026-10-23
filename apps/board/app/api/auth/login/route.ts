import { createClient } from "@/lib/supabase/server";
import { redirect } from "next/navigation";
import { headers } from "next/headers";

export async function POST() {
  const supabase = await createClient();
  const origin = (await headers()).get("origin") ?? "http://localhost:3000";
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: "google",
    options: {
      redirectTo: `${origin}/api/auth/callback`,
      queryParams: { hd: "linqapp.com", prompt: "select_account" }, // hint Google to the Linq domain
    },
  });
  if (error || !data.url) redirect("/login?error=oauth_failed");
  redirect(data.url);
}
