# API Design Exercise — "Design an API to store metrics"

Asked verbatim as Round 1 in the closest-matching Palo Alto SWE intern offer report (Apr 2025).
Even if you get a different prompt (design an alerts API, a service-appointment API), the
skeleton below transfers. Practice delivering this as a 20–25 min whiteboard conversation.

## Step 0 — clarify (always, out loud, ~2 min)
Who writes (devices? services?), write volume (events/sec?), read patterns (dashboards?
alerting? ad-hoc queries?), retention, latency needs, single metric types or arbitrary?
State assumptions if the interviewer says "you decide."

## Step 1 — API surface
```
POST /v1/metrics                  # ingest (support batching from day one)
  body: [{ "name": "vehicle.battery.temp",
           "value": 41.2,
           "timestamp": "2026-07-17T21:04:05Z",   # client ts; server records receive ts too
           "tags": { "vin": "5YJ3...", "region": "us-west", "fw": "2026.20.3" } }]
  → 202 Accepted  { "accepted": 2, "rejected": 0 }

GET /v1/metrics/{name}/query
  ?start=...&end=...&tags=region:us-west&agg=avg&step=1m
  → { "series": [ { "tags": {...}, "points": [[ts, value], ...] } ] }

GET /v1/metrics            # list/discover metric names (paginated)
```
Design decisions to speak to:
- **202 not 201**: ingestion is async; the write lands on a queue, not directly in the DB.
- **Batch endpoint**: per-event HTTP at high volume is dead on arrival.
- **Idempotency**: client-supplied event id or (name, tags, client-ts) dedup key — devices retry.
- **Validation & limits**: reject bad timestamps (clock skew window), cap tag cardinality,
  auth via token per client + rate limiting.
- **Versioned path** (`/v1/`), pagination cursors, consistent error envelope.

## Step 2 — storage
- Hot path: **time-series store** (or wide-column like Cassandra keyed by
  `(metric_name, tag_hash, time_bucket)`) — writes are append-heavy, queries are
  range-scans by time. Explain WHY a plain relational table hurts: index bloat on billions of
  rows, but note SQL is right for the metadata (metric catalog, dashboards, users).
- **Downsampling/rollups**: raw at 10s for 7 days → 1m for 90 days → 1h forever. Cuts storage
  and makes long-range queries fast.
- Mention cardinality as THE classic metrics-system killer (unbounded tag values like
  raw VIN in tags → millions of series).

## Step 3 — scale-up story (they will ask "now 100x traffic")
Client → LB → stateless ingest API (validates, writes to **Kafka**) → consumers batch-write to
the TS store → query service reads store + rollups, caches hot dashboard queries.
- Kafka gives buffering under burst, replay after consumer bugs, and multiple consumers
  (storage writer, streaming alert evaluator) from one stream — tie to their fleet-telemetry
  design which does exactly this.
- Partition by metric/tag hash for ordering per series; consumer lag is your health signal.

## Step 4 — observability of the system itself (JD checkbox — volunteer it)
Ingest rate, rejection rate, Kafka consumer lag, end-to-end freshness ("p99 event age at
query time"), query latency. Alert on freshness, not just error rate — stale-but-200 is the
sneaky failure mode. (This mirrors Tesla's own public data-platform talk: track end-to-end
freshness and coverage, not per-service latency.)

## Rehearsal plan
Day 9: deliver the whole thing out loud in 20 min to a wall/friend, drawing boxes.
Day 10: re-run it with a twist — "design the API for vehicles to report alerts" — and notice
it's the same skeleton (ingest → queue → store → query + freshness observability).
