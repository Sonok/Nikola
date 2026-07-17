# Probanker (SWE Intern, May–Aug 2025) — your strongest JD match

Why it matters here: Python backend + async job processing + monitoring = three of their
requirements in one story. Lead with this project when asked "tell me about a project."

## The 60-second architecture pitch (practice out loud)
"Multi-tenant Django backend serving university/corporate banking simulations. Web tier handles
REST requests; heavy simulation work is offloaded to Celery workers through a Redis broker;
results land in Postgres; Airflow schedules the batch ETL for market simulations; dashboards
track pipeline health. My work was hardening the async execution path and cutting the
simulation ETL runtime ~40%."

## Questions they WILL ask — prepare exact answers
- **"Walk me through what happens when a request comes in."** Request → Django view →
  validate + enqueue Celery task → worker picks it up from Redis → runs simulation step →
  writes results → client polls/receives status. Know your task states and what happens to
  in-flight tasks on worker crash (acks_late? retries? idempotency?).
- **"What does 'hardening async job execution' actually mean — what was broken?"** Have 2–3
  concrete failures: e.g. tasks lost on worker restart, duplicate execution, retry storms,
  queue backpressure during large scenario runs. For each: how detected, how fixed.
- **"How did you measure the 40%?"** Baseline end-to-end wall-clock of a representative
  scenario run before vs. after; which parts came from vectorization vs. the C/C++ extension
  vs. scheduling changes. If the honest answer is "roughly," say what you measured precisely
  and what's estimated.
- **"Why Celery/Redis and not Kafka/RabbitMQ?"** Honest answer: task-queue semantics (run this
  job once) vs. event-stream semantics (durable replayable log, many consumers). Celery fit
  the job-execution shape; Kafka fits fan-out telemetry. Showing you know the DIFFERENCE is
  the JD's "event-driven systems" box.
- **"Multi-tenant — how was isolation done?"** Know your actual mechanism (schema-per-tenant?
  tenant_id column + queryset scoping? routing?), and one risk (cross-tenant leak via missing
  filter) + how it was guarded.
- **"What did your monitoring dashboards actually track?"** Queue depth, task latency,
  failure/retry counts, throughput under large runs. Bonus sentence: "the JD's observability
  requirement — I've built exactly the freshness/health view a diagnostics pipeline needs."
- **"What SQL did you optimize?"** Have one real query story: N+1 from the ORM →
  select_related/prefetch_related, or an index that fixed a slow aggregate. Before/after
  numbers if you have them.

## Failure story (pick your real one and rehearse it)
Shape: symptom (jobs piling up / runs hanging) → how you localized it (logs? metrics? bisecting
scenario size?) → root cause → fix → the guard you added so it can't silently recur.

## Closing connection
"Their pipeline is the same shape at bigger scale: events in, async processing, results drive
a user-facing decision — and the monitoring I built is the part the JD calls observability."
