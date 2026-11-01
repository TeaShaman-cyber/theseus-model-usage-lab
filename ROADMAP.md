# Research roadmap — 2026-11-01

[Coordination issue #13](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/13) · [Repository scope](README.md) · [Cookbook lifecycle](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/operations/lifecycle.md)

## Purpose and boundaries

This lab owns the **research graph**: hypothesis → registered method → evidence → controlled analysis → reproducible receipt → interpretation / stop rule. Monitoring providers, public sensors, credentials, runtime repair and orchestration belong to their infrastructure owners. Data location does not grant authority over a scientific conclusion.

**Do not merge these claims:** HTTP success ≠ model-quality success; association ≠ causal effect; issue closed ≠ experiment accepted; Project card ≠ authority. Preserve FACT / INFERENCE / HYPOTHESIS / UNKNOWN, explicit UTC coverage and a test that could return a negative result.

## Current research graph

All listed issues were **OPEN** on GitHub at this snapshot. OPEN is a tracker state, **not** proof of active execution, acceptance or stale work. Where no verified terminal research receipt was found, the lifecycle disposition is **UNKNOWN** and must be triaged, not guessed.

| Track | Canonical issue(s) | Research dependency / next evidence |
| --- | --- | --- |
| A — provider usage and quotas | [#1](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/1) | Identify local activity vs control-plane quota; passive no-inference observation, schema and fail-open fixture |
| A — plugin design evidence | [#2](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/2), [#3](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/3) | Kanban failure history and publishability/distribution study; feed #1 design gate, no premature public release |
| B — model identity | [#4](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/4) | Per-turn provenance watermark measured against actual model route and session changes |
| B — credential boundaries | [#6](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/6) | Distinguish API-key, GitHub/OIDC and rotating OAuth authority; supports #9/#11 experiments |
| B — model/harness behavior | [#8](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/8) | Measure deterministic pre-tool guards against advisory-only rules; do not assume blocking is safer |
| C — independent model evaluation | [#5](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/5), [#7](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/7) | Multi-family mask-board research → bounded Nous-route council demonstration; preserve measured negative results and route truth |
| C — upstream contribution evidence | [#9](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/9), [#11](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/11) | Parent pipeline → Pilot A; deterministic regression ≠ stochastic behavior success ≠ upstream approval |
| D — model-serving anomaly | [#12](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/12) | DeepInfra/DeepSeek Oct 31–Nov 1: distinguish provider connection, long context, replay IDs, Hermes decisions using bounded existing traces |
| D — cross-layer physical hypothesis | [#14](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/14) | AI degradation × space-weather retrospective; preserve Observatory #11 preregistered controls, a NULL result as valid, and no causal overclaim |
| Coordination / housekeeping | [#13](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/13) | Confirm each issue disposition with receipts; govern README/roadmap, Project capability and PR audit |

## Research priorities — smallest useful next evidence

1. **#12:** one exact DeepInfra turn sequence around the registered connection error, with before/after successful calls and a separate behavioral outcome. No mixing with Nous route failures, no new inference calls just to probe. Link [local-lab #82](https://github.com/TeaShaman-cyber/local-lab/issues/82) for current missing per-call Loki↔Langfuse join-key limitation, [#124](https://github.com/TeaShaman-cyber/local-lab/issues/124) for post-hoc tool-trace audit, and [#89](https://github.com/TeaShaman-cyber/local-lab/issues/89) for output-truncation as a competing explanation.
2. **#14:** freeze Observatory canonical data range/head/health and run the *predeclared* same-window/event-deduplicated Kp/G-R-S discriminator with timestamp null and GitHub-status control. Do **not** optimize lag after seeing 31 Oct–1 Nov; that episode is motivating holdout, not independent validation.
3. **#9 / #11:** resolve whether [PR #10](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/pull/10) is reviewable/mergeable as a design input before any secret-bearing evaluation. Recheck exact head, CI/review and issue acceptance independently.
4. **#1–#8:** use existing terminal evidence to classify ACTIVE / PARKED / MIGRATED / SUPERSEDED / COMPLETED / HISTORICAL / UNKNOWN. Do not close by age, duplicate headings or 'everything OPEN' impression.

## Infrastructure evidence registry (references only)

- **Public observations:** [theseus-public-observatory](https://github.com/TeaShaman-cyber/theseus-public-observatory), canonical `data/YYYY-MM-DD/public-status.jsonl`. [Observatory #11](https://github.com/TeaShaman-cyber/theseus-public-observatory/issues/11) stores original OpenAI/Kp/G-R-S protocol; [space-weather lead ledger](https://github.com/TeaShaman-cyber/theseus-public-observatory/blob/main/docs/research/space-weather-llm-leads.md) stores leads, **not confirmed mechanisms**.
- **Hermes/provider current ops:** [local-lab #79](https://github.com/TeaShaman-cyber/local-lab/issues/79), [#81](https://github.com/TeaShaman-cyber/local-lab/issues/81), [#82](https://github.com/TeaShaman-cyber/local-lab/issues/82), [#89](https://github.com/TeaShaman-cyber/local-lab/issues/89), [#124](https://github.com/TeaShaman-cyber/local-lab/issues/124); operational documentation in `local-lab/docs/reference/observability/`. Historic [theseus-local-lab #58](https://github.com/TeaShaman-cyber/theseus-local-lab/issues/58), [#122](https://github.com/TeaShaman-cyber/theseus-local-lab/issues/122) and [#25](https://github.com/TeaShaman-cyber/theseus-local-lab/issues/25) remain provenance only.
- **Runtime read paths:** Grafana Loki/Tempo/Prometheus and Langfuse can supply measurements subject to current project boundaries; MarcoPolo is a governed workbench, not scientific acceptance. Do not mirror secrets, prompts, account data or private trace IDs into a public roadmap.

## Project V2 / issue hygiene

- **GitHub Project desired:** dedicated model-usage-lab issue-centered board. Minimum useful status projection: `Todo / In progress / Blocked / Done`; keep canonical lifecycle disposition in the issue, not in Project. Do not add custom fields without evidence of a need.
- **Current capability:** as verified 2026-11-01, governed `gh-write` can write repository issues/files but `gh project list --owner TeaShaman-cyber` reports missing `read:project` scope (also requires an authorized `project` write capability for board creation). **PROJECTS_BLOCKED_SCOPE; no board is claimed created.** A second profile returned blank/unusable Project metadata; do not treat it as authority or proof of absence. Only restore board work after user-controlled permission grant and exact Project/item readback.
- **Open design PR:** [#10](https://github.com/TeaShaman-cyber/theseus-model-usage-lab/pull/10) is not merged as of snapshot. Determine exact-head review/CI and whether the spec has drifted; do not auto-close or merge based on the roadmapping exercise.
- **Housekeeping rule:** retain historical evidence. For migration, identify target owner, preserve unresolved debt, create/read back target receipt, **then** disposition the source with appropriate authority. A copied hypothesis or link alone is not a completed migration.

## Minimal research receipt

For each accepted result store: `issue`, `research_question`, `hypotheses/null`, `source + exact Git SHA`, `UTC time window + coverage`, `protocol + preregistered controls`, `aggregate measurements`, `falsifiers`, `limitations`, `disposition`, `reproducer/receipt SHA`. A negative result is a result; missing telemetry is UNKNOWN, not zero.

Apply [Feynman checkpoint](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/methods/feynman-checkpoint.md) before adding machinery, and [Five Whys](https://github.com/TeaShaman-cyber/marcopolo-cookbook/blob/main/docs/methods/five-whys.md) to an evidenced failure; stop where another “why” becomes speculation.
