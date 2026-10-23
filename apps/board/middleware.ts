import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

const SUPA_URL = (process.env.NEXT_PUBLIC_SUPABASE_URL || process.env.SUPABASE_URL)!;
const SUPA_ANON = (process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || process.env.SUPABASE_ANON_KEY)!;

function hasAuthCookie(req: NextRequest) {
  return req.cookies.getAll().some((c) => c.name.startsWith("sb-"));
}

export async function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;
  // /login + /api handle their own auth.
  if (pathname.startsWith("/login") || pathname.startsWith("/api")) {
    return NextResponse.next({ request });
  }

  let res = NextResponse.next({ request });
  const supabase = createServerClient(SUPA_URL, SUPA_ANON, {
    cookies: {
      getAll() {
        return request.cookies.getAll();
      },
      setAll(cookies: { name: string; value: string; options: CookieOptions }[]) {
        cookies.forEach(({ name, value }) => request.cookies.set(name, value));
        res = NextResponse.next({ request });
        cookies.forEach(({ name, value, options }) => res.cookies.set(name, value, options));
      },
    },
  });

  try {
    const { data } = await supabase.auth.getSession();
    if (!data.session) return NextResponse.redirect(new URL("/login", request.url));
  } catch {
    if (hasAuthCookie(request)) return res; // transient blip — let the page load
    return NextResponse.redirect(new URL("/login", request.url));
  }
  return res;
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
