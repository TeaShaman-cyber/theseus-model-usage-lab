# Theseus Model Usage Lab

**Research repository** for model/provider behavior, usage and quota semantics, attribution, evaluation methods, agent reliability, and falsifiable cross-service hypotheses.

This repository owns **research questions → protocols → evidence-backed analysis → findings/disposition**. It is **not** the control plane for local Hermes, an observability backend, or the canonical archive of raw provider telemetry.

Start with [ROADMAP.md](ROADMAP.md) for the active research graph, issue inventory, dependencies and next verified steps.

## Evidence and execution boundaries

| Surface | Role | Authoritative for |
| --- | --- | --- |
| [Theseus Public Observatory](https://github.com/TeaShaman-cyber/theseus-public-observatory) | Public signals, source-health receipts, append-only records | Collected public observations (`data/YYYY-MM-DD/public-status.jsonl`), **not causal conclusions** |
| [local-lab](https://github.com/TeaShaman-cyber/local-lab) | Live Hermes/DeepInfra runtime and observability integration | Operational configuration and monitored system state |
| [theseus-local-lab](https://github.com/TeaShaman-cyber/theseus-local-lab) | Historical predecessor | Provenance only; not current runtime authority |
| Grafana / Loki / Tempo / Prometheus / Langfuse | Logs, metrics, traces and bounded telemetry inspection | Measurements in the verified project, time window and service |
| MarcoPolo / GitHub CI | Governed read/compute/workflows, versioned implementation and verification | Executed checks and scoped receipts, not research acceptance |
| **This lab** | Hypotheses, preregistration, control groups, reproducible analyses, decisions | Scientific interpretation and research acceptance |

## How a study progresses

1. State a testable claim, its counterhypotheses, operational definition, and **what would falsify it**.
2. Pin the exact data source, Git revision, UTC interval, model/provider route and coverage; label **FACT / INFERENCE / HYPOTHESIS / UNKNOWN**.
3. Apply predeclared controls and relevant independent checks. Preserve negative and inconclusive results.
4. Record a reproducible receipt and final research disposition in the owning issue; use a PR for durable code/docs.
5. Keep privacy boundaries: do not publish raw private sessions, prompts, credentials, billing/account records or trace IDs. Public aggregate/fixture results only.

A valid HTTP response is not proof of good model behavior; a correlation is not proof of causation; a green CI build is not scientific acceptance. Use the [cookbook lifecycle](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/operations/lifecycle.md), [Feynman checkpoint](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/methods/feynman-checkpoint.md) and [Five Whys](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/methods/five-whys.md) instead of inventing a second governance layer.

## Current research

- [#12 — DeepInfra / DeepSeek anomalies](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/12): trace-based analysis of a specific overnight behavioral incident.
- [#14 — AI degradation × space weather](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/14): controlled retrospective study, **hypothesis only; no causal finding**. Public Observatory [#11](https://github.com/TeaShaman-cyber/theseus-public-observatory/issues/11) preserves the earlier method and its evidence context.
- [#13 — roadmap and project coordination](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/13): research lifecycle and backlog audit, not a substitute for studies.

The full inventory, open PRs and Project capability state are in [ROADMAP.md](ROADMAP.md).
