# Domain Briefing — Tesla Remote Diagnostics (what Automated Diagnostics builds)

## The system end-to-end
1. **On the vehicle**: Tesla doesn't primarily use standard OBD-II DTCs. Cars generate
   proprietary **alerts** (e.g. `VCFRONT_a182`) — event-based fault records. Newer firmware
   attaches an **alert payload**: the actual CAN signal values at the moment the fault fired
   (e.g. the exact voltage on a "low voltage" alert). That payload is what makes accurate
   remote root-causing possible. Owners/techs see alerts in **Service Mode** on the
   touchscreen; **Service Mode+ / Toolbox 3** is the deeper tier (built by sibling teams in
   this same Service Engineering org).
2. **Connectivity**: vehicles hold persistent WebSocket connections to Tesla's backend — the
   internal messaging bus is called **Hermes** (protobuf-encoded, signed messages). Public
   blueprint: **github.com/teslamotors/fleet-telemetry** — vehicles push configurable telemetry
   as protobuf over WebSocket; the server dispatches three stream types (telemetry records,
   connectivity records, alerts/errors) with **Kafka recommended for production**, Prometheus
   metrics and structured JSON logging built in. **Read that README — highest-leverage hour of
   domain prep available.**
3. **Data platform scale**: Tesla has publicly cited ~**30M events/sec peak, trillions of
   events/day through Kafka** (InfoQ talk by a founding data-platform engineer). Their stated
   design lessons: isolate pipelines by business unit/model/geo; push raw data fast and
   sanitize in the cloud; track **end-to-end freshness and coverage**, not just per-service
   latency.
4. **The funnel this team owns**: customer describes an issue in the Tesla App (free text) →
   automated remote **pre-diagnosis** runs against the vehicle → branch:
   **self-service guidance** · **remote/OTA fix** · **mobile service** dispatch (van arrives
   with parts pre-loaded) · **service-center appointment** with parts pre-ordered and the
   estimate pushed to the app. Success metrics: **deflection rate, first-time-fix rate,
   parts-prediction accuracy**.
5. **Where ML fits**: streaming anomaly detection on telemetry (Kafka consumer + model
   serving); predictive-failure models; request-time NLP triage fusing the customer's free
   text with the vehicle's alert history to classify the issue and pre-pick parts.
   (Published work exists on NLP over free-text vehicle service reports — arXiv:2111.14977.)

## Vocabulary
alert vs. DTC · alert payload · telemetry · OTA · triage · pre-diagnosis ·
Service Mode / Toolbox 3 · Hermes · Mobile Service · deflection rate · first-time fix ·
freshness/coverage

## Three anecdotes to memorize
1. **2019 Power Conversion System story**: a Model 3 detected its own fault, pre-shipped the
   replacement part to the owner's preferred service center, THEN notified the owner. Tesla:
   "skipping the doctor and going right to the pharmacy." The end-state this team automates
   toward.
2. **Economics**: dealerships make roughly half their gross profit on service; Tesla has no
   dealers, so service is pure cost — every remotely-resolved issue is direct margin. Mobile
   service is ~40% of North American visits and only works if remote diagnosis + parts
   prediction are right the first time. (Avoid the "90% resolved remotely" stat — third-party,
   not Tesla-sourced.)
3. **OTA as remote fix**: recalls fixed entirely in software — window-pinch recall (1M+ cars),
   FSD phantom-braking recall, and the 2018 OTA that shortened Model 3 braking distance after
   Consumer Reports criticism.

## Sources
teslamotors/fleet-telemetry (GitHub) · InfoQ "Designing IoT Data Pipelines for Deep
Observability" · Electrek (2019 pre-shipped-part story; 2022 in-app self-diagnosis) · Tesla
service/support pages · Shop Owner Mag (diagnostics tiers) · Not a Tesla App (Service Mode,
alert payloads) · tesla-api GitHub Hermes discussion · Consumer Reports (OTA recalls) ·
arXiv:2111.14977
