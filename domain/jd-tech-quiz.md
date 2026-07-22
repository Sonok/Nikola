# JD Tech Quiz — 20 questions (answers at the bottom, no peeking)

Companion to jd-tech-breakdown.md. Rules: answer OUT LOUD in 1–3 sentences before
checking. Score yourself ✓ / half / ✗. Anything below ✓ gets retested Thursday.
Questions marked ★ are ones an interviewer could genuinely ask on Monday.

## A. APIs
1. ★ Why does a retried POST need an idempotency key, but a retried DELETE doesn't?
2. Design smell: what's wrong with `GET /getVehicleAlerts?vin=123`, and what should
   it be?
3. ★ Your appointment-creation endpoint returns 200 with `{"error": "vehicle not
   found"}` in the body. Why is that bad?

## B. Distributed systems
4. ★ Your consumer received the same "alert fired" event twice. Is that a bug in the
   pipeline? What must YOUR code do about it?
5. What does backpressure mean, and where does it show up in fleet-telemetry when
   Kafka is down? (deep-dive §7 overlap)
6. ★ Explain at-least-once vs. at-most-once delivery, and which one a diagnostics
   pipeline should choose and why.
7. Your one-liner: what's your strongest distributed-systems experience card?

## C. Event-driven systems
8. ★ Kafka vs. RabbitMQ in one breath: when is each the right tool?
9. What does partitioning a Kafka topic by VIN buy you, and what does it NOT
   guarantee?
10. What's a consumer group, and why can triage, analytics, and alert-history all
    read the same topic without stealing each other's messages?
11. ★ What's a dead-letter queue and when does a message end up there?

## D. Applied ML
12. ★ The JD says "model deployment, inference pipelines, or ML system integration"
    — NOT research. In one sentence each, what are your three integration stories?
13. Why is the model loaded at service startup instead of inside the request handler?
14. ★ Where do the team's two ML shapes live: which one is streaming, which one is
    request-time, and what data does each consume?

## E. Databases
15. ★ Appointments, alert history, hot per-VIN diagnosis cache: pick a store for each
    and justify in one sentence per pick.
16. Write (out loud or on paper) the SQL for "top 5 alert codes fired in the last
    24 hours." No peeking at section 7's snippet first.

## F. Observability
17. ★ Name the three pillars, plus the fourth thing Tesla's data-platform talks add —
    and why per-service latency alone is a lie in a pipeline.
18. What's a trace ID, and what is the full path it should follow in the diagnosis
    funnel?

## G. Python / backend
19. When do you reach for deque over list, and defaultdict over dict? One concrete
    use from YOUR recent solutions for each.

## H. The one that isn't about tech
20. ★ "Tell me about a failure you troubleshot end-to-end." Say your METHOD in four
    words, then the story in 60 seconds. (Rubric: reproduce → localize → hypothesize
    → verify, a real cost, a changed habit.)

---
---
---

# Answers (grade yourself honestly)

1. POST creates — two retries = two appointments. An idempotency key lets the server
   detect the duplicate and return the original result. DELETE is naturally
   idempotent: deleting twice leaves the same end state (gone).
2. Verb in the URL and a query param doing a path's job. Method supplies the verb:
   `GET /v1/vehicles/123/alerts`.
3. Status codes are the contract — clients, retry logic, and monitoring key off them.
   A 200-with-error is invisible to all three: dashboards stay green while users
   fail. Return 404.
4. Not a bug — at-least-once delivery guarantees duplicates under retry. The consumer
   must be idempotent: dedupe on event ID (seen-set/table) before acting.
5. Backpressure = downstream slowness propagating upstream as a signal instead of
   data loss. In fleet-telemetry: Kafka down → producer buffer fills (~1M msgs) →
   acks stop → vehicle holds/retransmits records. The edge slows; nothing is lost.
6. At-least-once: never lose a message, but duplicates possible (ack after durable
   write; retransmit if no ack). At-most-once: never duplicate, but can lose. A
   missed fault record is a missed diagnosis — diagnostics picks at-least-once and
   dedupes downstream.
7. (Yours, but the shape:) "MPI sample sort across 256 simulated nodes / 5 topologies
   — measured communication bottlenecks; plus replay tooling that validates
   distributed behavior against production-scale workloads."
8. Kafka: durable, replayable, partitioned LOG — many independent readers of the same
   stream (analytics + triage + storage). RabbitMQ: QUEUE for task distribution — a
   job goes to exactly one worker. Streams of facts → Kafka; jobs to do → queue.
9. Buys: all events for one vehicle land in one partition → strict per-vehicle
   ordering, and parallelism across vehicles. Does NOT guarantee: global ordering
   across VINs, or balanced load if a few VINs are extremely chatty.
10. A consumer group shares a topic's partitions among its members — each partition
    is read by exactly one member per group. Different GROUPS each get the full
    stream with their own offsets. Triage, analytics, history = three groups.
11. A parking spot for messages that repeatedly fail processing (poison messages).
    After N failed retries, the consumer ships the message + error context there so
    the partition isn't blocked, and something alerts a human.
12. State Street: BERT/Vader inference pipeline over 10k+ daily filings. Event
    discovery: sentence-transformer embeddings + cosine ranking served from Cloud
    Functions. UMD: anomaly-detection models over machine-generated logs.
13. Loading is slow and memory-heavy (deserialize weights); per-request loading adds
    seconds of latency and multiplies memory. Load once, serve many — and it fails
    fast at startup if the artifact is bad, not on a customer request.
14. Streaming: anomaly/predictive detection as a Kafka consumer over telemetry.
    Request-time: NLP triage at the moment a customer files a complaint — fuses their
    free text with the vehicle's alert history to classify and pre-pick parts.
15. Appointments: relational/Postgres — transactions, joins to vehicles/parts/slots.
    Alert history: wide-column/time-series — append-heavy, TTL, scan by VIN+time.
    Hot cache: Redis — key-value with TTL, `diag:{vin}` → result.
16. `SELECT code, COUNT(*) AS n FROM alerts WHERE fired_at > now() - interval '24
    hours' GROUP BY code ORDER BY n DESC LIMIT 5;` (Credit for: aggregate, filter,
    group, order, limit — that's the reported difficulty level.)
17. Metrics, logging, tracing + freshness/coverage. Per-service latency can be green
    while data is hours stale or a vehicle went silent — end-to-end "when did we
    last hear from this car, and how old is the data we diagnosed on" is the truth.
18. A unique ID minted at the entry point and propagated through every hop: app →
    diagnosis API → vehicle command/telemetry → result → parts/appointment — so one
    slow or wrong diagnosis can be reconstructed across services.
19. deque: O(1) pops from the left — BFS queues (909 today, 200, 2115). defaultdict:
    grouping without key-existence checks — adjacency lists in 207/2115
    (`defaultdict(list)`), counting (`defaultdict(int)`).
20. Method: reproduce → localize → hypothesize → verify. Story must include a real
    cost and the safeguard you adopted. If your 60-second version rambles past 90,
    cut scene-setting, keep the method visible.
