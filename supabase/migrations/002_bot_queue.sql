-- ============================================================================
-- Serverless bot backend: a job queue + a durable thread→project map.
--
-- The bot is moving off the Mac (Socket Mode daemon) to Vercel (Events API):
--   • a fast endpoint verifies the Slack signature, enqueues a job, acks < 3s
--   • a worker (cron / triggered function) drains the queue and runs the build
-- Vercel functions have a read-only FS + don't share /tmp across invocations,
-- so the thread map that used to live in brands/.threads.json moves here.
-- ============================================================================

create table if not exists amb_job (
  id            bigint generated always as identity primary key,
  status        text not null default 'queued',   -- queued | running | done | failed
  action        text not null,                    -- build | storyboard | brand-doc | review | feedback | status
  brand         text not null,
  channel       text,
  thread_ts     text,
  user_id       text,
  files         jsonb not null default '[]'::jsonb, -- [{name, url}]
  note          text,
  result        text,
  error         text,
  attempts      int not null default 0,
  created_at    timestamptz not null default now(),
  started_at    timestamptz,
  completed_at  timestamptz
);

-- Worker picks the oldest queued job; index the drain path.
create index if not exists amb_job_queued_idx on amb_job (created_at) where status = 'queued';

-- Dedup: Slack retries events; don't enqueue the same event twice.
alter table amb_job add column if not exists slack_event_id text;
create unique index if not exists amb_job_event_uq on amb_job (slack_event_id) where slack_event_id is not null;

-- Durable thread → project map (replaces brands/.threads.json).
create table if not exists amb_thread (
  channel     text not null,
  thread_ts   text not null,
  brand       text not null,
  updated_at  timestamptz not null default now(),
  primary key (channel, thread_ts)
);
