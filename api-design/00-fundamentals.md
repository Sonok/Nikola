# API Fundamentals — read this BEFORE metrics-api.md

Zero-assumed-knowledge tour of everything an interviewer means when they say "design an API."

## 1. What an API actually is here
A web API is a contract: "send an HTTP request shaped like X to URL Y, get back a JSON response
shaped like Z." Your job in the interview is to define the URLs, the shapes, and the rules.

## 2. The HTTP methods (verbs)
| Method | Meaning | Example | Notes |
|---|---|---|---|
| **GET** | Read data. Never changes anything. | `GET /vehicles/123/alerts` | Safe to retry/cache. No request body. |
| **POST** | Create something new / trigger an action. | `POST /appointments` with JSON body | NOT idempotent: sending twice creates two. |
| **PUT** | Replace a thing entirely at a known URL. | `PUT /users/42/settings` | Idempotent: sending twice = same result. |
| **PATCH** | Partially update a thing. | `PATCH /appointments/9` body `{"time": "10:00"}` | Only send fields that change. |
| **DELETE** | Remove a thing. | `DELETE /appointments/9` | Idempotent: deleting twice is still gone. |

**Idempotent** = doing it N times has the same effect as doing it once. This word WILL come up.
Interview line: "POST isn't idempotent, so if clients retry on timeout we need an idempotency
key so we don't double-create."

## 3. URL design (REST conventions)
- URLs name **things (nouns), plural**; the method supplies the verb:
  - Good: `POST /appointments` (create), `GET /appointments/9` (read one)
  - Bad: `POST /createAppointment`, `GET /getAppointmentById?id=9`
- Nesting shows ownership: `GET /vehicles/123/alerts` = alerts belonging to vehicle 123.
- **Path** = which thing (`/vehicles/123`). **Query params** = how to filter/sort/page
  (`?status=open&sort=-created_at&limit=50`).
- Version the whole thing: `/v1/...` — so you can change the contract later without breaking
  old clients.

## 4. Anatomy of request and response
```
Request:  POST /v1/appointments
          Headers: Authorization: Bearer <token>     ← who you are
                   Content-Type: application/json    ← body format
          Body:    {"vehicle_id": "123", "issue": "clunk over bumps"}

Response: Status: 201 Created
          Body:   {"id": "apt_9", "vehicle_id": "123", "status": "scheduled",
                   "created_at": "2026-07-17T21:00:00Z"}
```
Convention: the create response echoes the full object including its new server-assigned `id`.

## 5. Status codes (know ~10)
| Code | Meaning | When |
|---|---|---|
| 200 OK | success | GET/PATCH/PUT worked |
| 201 Created | made a new thing | successful POST |
| 202 Accepted | "got it, working on it" | async work (queued, not done yet) |
| 204 No Content | success, nothing to return | DELETE |
| 400 Bad Request | client sent garbage | invalid JSON, missing field |
| 401 Unauthorized | who are you? | missing/bad auth token |
| 403 Forbidden | you can't touch that | valid user, wrong permissions |
| 404 Not Found | no such thing | bad id in the URL |
| 409 Conflict | state collision | double-booking, duplicate create |
| 429 Too Many Requests | slow down | rate limit hit |
| 500 / 503 | server broke / overloaded | your bug / retry later |
Rule of thumb: 4xx = caller's fault, 5xx = server's fault.

## 6. The requirements checklist (what "requirements" means in this exercise)
Ask/state these before designing — this IS the rubric:
1. **Who calls it?** (mobile app? other services? vehicles?) → auth style, payload size
2. **Read-heavy or write-heavy?** → caching vs. ingestion queue
3. **Scale?** requests/sec now and 10x → where does it break first
4. **Latency needs?** interactive (<200ms) vs. batch/async
5. **What can be eventually consistent?** → what can go through a queue
6. **Retention/history?** → storage growth, archival

## 7. The universal answer outline (memorize this order)
1. **Clarify requirements** (the checklist above, 2 min, out loud)
2. **Resources**: list the nouns (metrics, alerts, appointments...)
3. **Endpoints**: table of method + path + one-line purpose
4. **Sample request/response JSON** for the 1–2 most important endpoints
5. **Status codes + errors**: one consistent error shape:
   `{"error": {"code": "invalid_vehicle", "message": "..."}}`
6. **Data storage**: what table/collection per resource, SQL vs NoSQL one-liner
7. **The -ilities** (say each in one sentence):
   - auth: Bearer token on every request
   - pagination: `?limit=50&cursor=abc` (never return unbounded lists)
   - rate limiting: per-client token bucket → 429
   - idempotency: client-supplied `Idempotency-Key` header on POSTs
   - versioning: `/v1/`
8. **Scale-up story**: stateless API servers behind a load balancer → queue (Kafka) for heavy
   writes → cache (Redis) for hot reads → monitoring on rate/errors/latency
Steps 1–4 are the core; 5–8 are where you sound senior. If short on time, do 1–4 well.

## 8. Worked mini-example (30-second version, different from metrics so you have two)
"Design an API for service appointments":
```
POST   /v1/appointments               create (409 if slot taken)
GET    /v1/appointments/{id}          read one
GET    /v1/appointments?vehicle=123&status=open   list, filtered + paginated
PATCH  /v1/appointments/{id}          reschedule/update
DELETE /v1/appointments/{id}          cancel (204)
```
Storage: SQL (transactions matter — two people must not book one slot).
Auth: bearer token; a user only sees their own vehicle's appointments (403 otherwise).

Then go to `metrics-api.md` — it's this same outline applied to the question Tesla actually
asked, plus the Kafka/time-series depth.
