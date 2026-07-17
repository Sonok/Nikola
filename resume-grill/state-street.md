# State Street / UCONN — NLP Sentiment Pipeline (May–Aug 2023)

Why it matters here: their triage system does NLP on the customer's free-text issue description
("my car clunks over bumps") fused with vehicle data. Your BERT/Vader pipeline on SEC filings is
your evidence you've done applied NLP end-to-end, not just a class project.

## The 60-second pitch
"Co-led an equity sentiment project with State Street: GCP ETL pipeline ingesting 10K+ daily SEC
filings and news into analysis-ready feature stores; NLP factor models using BERT embeddings and
VaderSentiment; backtested against baselines, cutting out-of-sample MSE ~20%; results surfaced
in Tableau dashboards; published a write-up and open-sourced the frontend."

## Questions they WILL ask
- **"BERT vs. Vader — why both?"** Vader: lexicon-based, fast, cheap, decent on short/financial
  text with tuning; BERT: contextual embeddings, catches negation and nuance, costs GPU time.
  Know which fed which model and what each contributed to the final signal.
- **"What does 20% MSE reduction mean concretely?"** Against WHAT baseline, on what holdout,
  out-of-sample how (walk-forward? single split?). If the baseline was naive (prior-day value /
  no-sentiment model), say so plainly — a precise modest claim beats a vague grand one.
- **"How did you avoid lookahead bias?"** Filing timestamps vs. trading windows; features only
  from data available at prediction time. (They may not know finance, but "how did you prevent
  the model from cheating" is a universal ML question — this is your answer.)
- **"10K filings/day — walk me through the ETL."** Source → parse (what format? XBRL/HTML
  mess?) → normalize → feature store schema → what breaks (malformed filings, rate limits,
  dedup) and how the pipeline handled it.
- **"What was YOUR slice vs. the team's?"** You co-led — be specific about the parts you
  personally built vs. directed.

## Closing connection
"Their triage problem is harder and more interesting: fuse free-text customer language with
structured vehicle alerts. But 'messy human text in, decision-grade signal out, with a pipeline
that runs every day unattended' is exactly what I built here."
