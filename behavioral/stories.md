# Behavioral — story bank

Tesla folds behavioral into every round (~15 min of each engineer interview). Recurring themes
from candidate reports: Why Tesla / passion for the product, a bug nobody else could fix,
learning something new fast, lessons from failure. Answer shape: situation in one sentence →
what YOU did → measurable outcome → what changed in how you work.

## Why Tesla / why this team (60–90 seconds — write your own words, hit these beats)
- Product pull: genuine interest in vehicles that are software-defined — service problems that
  get FIXED by software (OTA recalls) instead of recalls-by-mail.
- Team fit: "my background is literally the three pieces of this team's stack" — async Python
  backends (Probanker), ML on machine-generated logs (UMD anomaly detection), NLP on messy
  human text (State Street). You're not pivoting; you're converging.
- The mission line that's actually credible: service is the #1 owner complaint and the team's
  work is the fix at fleet scale — user-facing impact with hard engineering underneath.
- DON'T: recite Tesla facts without a personal thread, or say "I love cars" with nothing
  behind it. If you have a real story of a car problem that a remote diagnosis would have
  solved, open with it.

## Story slots to fill (write 4–6 bullet outlines, rehearse out loud Days 9–10)
1. **Hardest bug** — best candidate: a Probanker async/Celery failure or the UMD pipeline
   break. Must include your debugging METHOD (reproduce → localize → hypothesize → verify),
   not just the fix. This team diagnoses failures for a living; the method is the answer.
2. **Learned something fast** — e.g., OpenMP/C extensions for the simulation core, or PySpark
   for the honeypot dataset. Emphasize the learning loop you used, and the deadline.
3. **Disagreement / feedback** — a design disagreement or code-review pushback and how it
   resolved. Outcome must include what YOU changed.
4. **Failure / mistake** — pick a real one with a real cost, own it cleanly, name the
   safeguard you now use. Interviewers pattern-match evasiveness here.
5. **Impact you're proud of** — the 40% ETL speedup or the anomaly-detection pipeline
   end-to-end. Lead with the number, then how.
6. **Working with non-engineers / users** — Probanker's university clients or the State
   Street stakeholders; translating requirements into technical decisions.

## Questions to ask THEM (have 3 ready; these signal domain prep)
- "What fraction of service requests can be fully pre-diagnosed before a human touches them
  today, and where does the funnel leak most — detection, classification, or parts prediction?"
- "When the model and the customer's description disagree, who wins — and how do you measure
  false 'no fault found' outcomes?"
- "What does an intern own end-to-end in 12 weeks on this team?"
- "How does the team consume fleet telemetry — do you sit directly on the Kafka streams the
  data platform exposes, or behind an internal API?"

## Logistics answers to have ready (truthful, one sentence each)
- Grad date: December 2027 (in range for the posting's Dec 2027–Dec 2028 requirement).
- Availability: full-time onsite in Palo Alto for the entire ~Aug–Dec term.
- Current internship end date and any conflicts — clean, honest answer prepared BEFORE the
  recruiter screen (see resume-grill/README.md consistency notes).
