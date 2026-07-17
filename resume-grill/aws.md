# AWS (SDE Intern, Networking Infrastructure — summer 2026, current)

You're in this internship right now, which makes it the most likely "so what are you working on
today?" question — and the easiest place to get caught overstating. Keep this one scrupulously
accurate and scoped: you're partway through the internship, so describe work in progress
honestly ("I'm building / so far I've...").

## The 60-second pitch (adjust to what you've actually done by interview day)
"SDE intern on Networking Infrastructure. I'm working on data ingestion/processing for
high-volume network telemetry — streaming pipelines where the concerns are throughput, latency,
and fault tolerance. It's my first exposure to systems at AWS scale, and it's taught me how
different design gets when every component must assume its dependencies will fail."

## Questions they WILL ask
- **"What exactly are you building?"** Have one concrete, specific artifact you own — a
  component, a test harness, a metric pipeline — described at the level of inputs/outputs and
  the design choice you made. (Respect AWS confidentiality: describe shape and scale class,
  not internal service names/numbers you shouldn't share — saying that out loud reads as
  professionalism, not evasion.)
- **"What's hard about network telemetry at scale?"** Volume vs. fidelity trade-offs
  (sampling/aggregation), late and out-of-order data, backpressure, cardinality explosion in
  metrics, cost of retaining raw vs. rolled-up data.
- **"What have you learned from AWS code review culture?"** Have a real example of feedback
  that changed how you write code.
- **Timeline logistics** — be ready for "when does your internship end / when can you start?"
  with a clean, truthful answer that fits this role's ~August start.

## Closing connection
"Network telemetry and vehicle telemetry are cousins: huge event volume, most of it boring,
and the whole game is reliably surfacing the events that mean something — that's why this
team's problem clicked for me."
