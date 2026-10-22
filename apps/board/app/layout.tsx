export const metadata = { title: "AMB Approval Board", description: "Apple Messages for Business approval pipeline" };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: "-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif", background: "#f4f6f8", color: "#1b2430" }}>
        <div style={{ maxWidth: 1180, margin: "0 auto", padding: "28px 24px" }}>{children}</div>
      </body>
    </html>
  );
}
