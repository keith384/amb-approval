-- AMB Approval pipeline — state + tracking store (shared Supabase project).
-- Artifacts live in Slack; this stores pipeline state + links for the board.

create table if not exists amb_brand (
  id uuid primary key default gen_random_uuid(),
  name text unique not null,
  stage text check (stage in ('brand_approval','ux_approval','experience_review','launch','launched')),
  owner text,
  stage_entered_at timestamptz,
  last_apple_touch timestamptz,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table if not exists amb_event (
  id bigint generated always as identity primary key,
  brand text not null,
  action text not null,          -- brand_doc | storyboard | review | stage_moved | sent_to_apple | apple_feedback | owner_set
  detail text,
  at timestamptz default now()
);
create index if not exists amb_event_brand on amb_event(brand, at desc);

create table if not exists amb_artifact (
  id bigint generated always as identity primary key,
  brand text not null,
  stage text,
  kind text,                     -- doc | usecases_form | readiness_form | storyboard | review | timestamp_index | scope | readiness_note
  label text,                    -- filename / title
  link text,                     -- Slack permalink (or path until uploaded)
  created_at timestamptz default now()
);
create index if not exists amb_artifact_brand on amb_artifact(brand, created_at desc);

alter table amb_brand enable row level security;
alter table amb_event enable row level security;
alter table amb_artifact enable row level security;
-- Internal tool: reads via authenticated (board SSO), writes via service role (bypasses RLS).
create policy amb_read_brand on amb_brand for select to authenticated using (true);
create policy amb_read_event on amb_event for select to authenticated using (true);
create policy amb_read_artifact on amb_artifact for select to authenticated using (true);
