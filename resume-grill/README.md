# Resume Grill — how Tesla runs it

Tesla interviewers routinely spend **20–30 minutes interrogating specific resume projects before
any coding** — in one report the grilling ran so long only 20 minutes remained for the coding
task. They pick a bullet and drill: what exactly did YOU build, why that design, what broke, what
were the numbers, what would you change. Vague answers end interviews.

## Rules for every answer
1. **Own a specific slice.** "The team built X; the part I owned was Y" beats claiming everything.
2. **Have the architecture diagram in your head** — be able to draw each project on a whiteboard
   in 60 seconds: boxes, arrows, where data enters and exits.
3. **Know your numbers and how they were measured.** Every metric on the resume ("40% faster",
   "10K+ daily filings") will get a "how did you measure that?" Have the before/after method.
4. **Have one failure story per project** — what broke, how you debugged it, what you changed.
   This team diagnoses failures for a living; debugging methodology is the hidden rubric.
5. **End answers with the connection**: one sentence tying the project to remote diagnostics
   (streaming data, triage, anomaly detection, pipeline observability).

## Files
- `probanker.md` — backend/eventing story (strongest JD match)
- `umd-anomaly-detection.md` — ML-on-logs story (structurally identical to their core problem)
- `state-street.md` — NLP/ETL story (maps to their free-text triage)
- `aws.md` — current internship (keep it accurate and scoped)

## ⚠ Consistency risks — read before any interview
The submitted resume (`Sonok_Tesla.pdf`) differs from the real one (`Sonok_Resume.pdf`). These
differences are exactly where a 30-minute grill goes wrong, and post-offer background checks
verify employer, title, dates, and degrees:

- **Shopify Sept–Dec 2026 line directly conflicts with this internship's term** (Aug–Nov/Dec,
  onsite Palo Alto). Expect "aren't you committed to Shopify this fall?" in the first call.
  Have a truthful answer ready.
- **AWS entry**: submitted says "SDE, AWS Security (Rubicon)"; actual role is SDE *Intern*,
  Networking Infrastructure. Employment verification surfaces title/team/dates mismatches.
- **Degree line**: submitted lists an M.S.; education verification pulls registrar records.
- Items on the submitted resume that aren't real can't be prepped in this folder — there's no
  depth to drill into, and the grill format is specifically designed to find that out. The
  defensible move is to steer every conversation to the real projects below (they're a genuinely
  strong match for this JD) and to correct the record with the recruiter where you can.
