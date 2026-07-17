# Interview Talking Points — say these, in roughly this order of value

1. **The one-sentence frame**: "This team is a funnel-optimization problem on top of a
   streaming platform" — product = the self-service / remote-fix / mobile / service-center
   decision funnel; platform = Kafka-carried telemetry and alerts; metrics = deflection rate,
   first-time-fix rate, parts-prediction accuracy. Shows you get product AND architecture.

2. **Alerts-with-payload beat DTCs**: event records carrying actual CAN signal values at fault
   time make remote root-causing feasible — "I'd design triage to consume the alert payload
   plus telemetry context, not just the alert code."

3. **fleet-telemetry as the public blueprint**: WebSocket + protobuf in, Kafka out, separate
   telemetry/connectivity/alert streams, Prometheus built in. Referencing a repo THEY
   open-sourced is the cheapest possible credibility.

4. **Scale realism**: ~30M events/sec peak, trillions/day through Kafka, and Tesla's own
   stated lessons — pipeline isolation, cloud-side sanitization, end-to-end freshness
   observability. Use when asked about distributed systems.

5. **ML placement**: streaming inference on telemetry for anomaly/predictive alerts, plus
   request-time inference fusing NLP on the customer's free text with alert history to
   classify the issue and pre-pick parts.

6. **The killer anecdote**: 2019 — car detects its own Power Conversion System fault,
   pre-ships the part, then tells the owner. "Skipping the doctor and going right to the
   pharmacy."

7. **Economics in one sentence**: no dealer network means service is pure cost, so automated
   remote diagnosis is how service capacity scales sub-linearly with a fleet growing by
   ~1.5M+ vehicles/year — and it's why mobile service (~40% of NA visits) works at all.

8. **Observability as product correctness**: a wrong remote diagnosis ships the wrong part to
   a van. Tracing one request across app → API → Hermes/vehicle → diagnostic result → parts
   order, plus data-freshness monitoring, is core — not an afterthought.

9. **Failure modes to volunteer unprompted** (sounds senior):
   - vehicle offline when the diagnostic triggers → async retry/queueing, idempotency
   - customer's description disagrees with telemetry → signal fusion, rules + ML hybrid
   - precision/recall asymmetry: a false "no fault found" that turns away a real problem
     costs far more than an unnecessary appointment

10. **Org awareness**: Toolbox 3 / remote-diagnostics access is now sold to independent shops
    (right-to-repair), built by sibling teams in the same Service Engineering org — shows you
    understand the org's full surface, not just your team.
