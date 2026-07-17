# UMD — Anomaly Detection on Network Logs (Jun–Aug 2024)

Why it matters here: **structurally identical to the team's core ML problem.** You took a large
stream of machine-generated logs (450K honeypot records), engineered features, trained an anomaly
classifier, evaluated with precision/recall, and automated the pipeline. Swap "network logs" for
"vehicle telemetry/alerts" and it's their job. Say that mapping out loud — it's your best line.

## The 60-second pitch
"AWS-hosted honeypot generated 450K+ raw network log records. I built the end-to-end pipeline:
ingestion and cleaning, feature engineering in Pandas/PySpark (country mapping, port rollups,
protocol encoding, time-of-day buckets), a Random Forest anomaly classifier evaluated on
precision/recall/F1, feature-importance analysis to find highest-signal attributes, and
dashboards/heatmaps on top — all automated with Docker + CI."

## Questions they WILL ask
- **"Why Random Forest?"** Tabular features, mixed types, no scaling needed, robust to
  outliers, interpretable via feature importance. Know what you compared it against (logistic
  regression baseline? XGBoost?) and why RF won or was chosen.
- **"How were labels defined?"** Honeypot traffic is hostile-by-default — be precise about what
  counted as anomalous vs. normal and where labels came from. If labeling was heuristic, own it
  and explain the limitation.
- **"Class imbalance?"** Anomalies are rare. What you did (class weights? resampling? threshold
  tuning?) and why accuracy is the wrong metric — that's WHY you report precision/recall/F1.
- **"Precision vs. recall — which mattered more and why?"** Have a position. Then land the
  team-relevant asymmetry: for vehicle diagnostics, a false 'no fault found' that turns away a
  real problem costs far more than an unnecessary appointment — so you'd tune for recall on
  safety-relevant faults and manage precision with a human-review tier.
- **"What did feature importance tell you?"** Name your top 2–3 features and the story they told.
- **"Schema inconsistencies at scale — like what?"** Concrete examples: mixed types, missing
  fields, format drift between log batches. How you detected and normalized them. (This is a
  real problem in vehicle telemetry across firmware versions — say so.)
- **"How would this run in production instead of batch?"** Your upgrade path: stream in via
  Kafka, feature computation on a consumer, model behind an inference service, monitor input
  drift and score distribution, retrain cadence. This answer covers the JD's "applied ML —
  model deployment, inference pipelines" box.

## Failure story
Have one: e.g., a feature that leaked label information, a schema change that silently broke
the pipeline, an early model that looked great on accuracy and useless on recall.

## Closing connection
"Fleet telemetry is this exact problem with better data: alerts carry the CAN signal payload at
fault time, so the features are richer — but the pipeline shape (ingest → featurize → classify →
route a decision) is the same one I built."
