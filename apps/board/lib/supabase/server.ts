import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

// Session-scoped client (anon key + auth cookies) for Google sign-in / session reads.
// Data access stays on the service-role client in lib/db.ts.
const URL = (process.env.NEXT_PUBLIC_SUPABASE_URL || process.env.SUPABASE_URL)!;
const ANON = (process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || process.env.SUPABASE_ANON_KEY)!;

export async function createClient() {
  const cookieStore = await cookies();
  return createServerClient(URL, ANON, {
    cookies: {
      getAll() {
        return cookieStore.getAll();
      },
      setAll(cookiesToSet: { name: string; value: string; options: Record<string, unknown> }[]) {
        try {
          cookiesToSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options));
        } catch {
          /* called from a Server Component — middleware refreshes the session cookie */
        }
      },
    },
  });
}
