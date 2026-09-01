# Nous route council experiment — 2026-09-02

Experiment: `ISSUE-20260901-NOUS-ROUTE-COUNCIL-EXPERIMENT`
GitHub issue: https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/7

This run tests whether independent role masks improve a practical diagnostic-tool design over a parent baseline. Model outputs are evidence for synthesis, not operational truth. No council recommendation changes the Nous runtime.

## Protocol

- Five independent masks per executor: `ARCHIVIST`, `PRACTITIONER`, `SYSTEMS_ENGINEER`, `NEWCOMER`, `SKEPTIC`.
- Fixed task packet and JSON response schema across executor routes.
- Sentinel before each executor pass.
- Free routes before paid routes; OpenAI `Sol` is last.
- One bounded retry is allowed after a transient executor capacity failure.
- Facts, assumptions, hypotheses, next tests, verdict, confidence, and weakest point remain separate.
- No tools, memory access, file writes, config changes, Hindsight writes, or credentials in child passes.

## Current pass ledger

| Pass | Executor | Sentinel | Council result |
|---|---|---:|---:|
| 1 | `nous / meituan/longcat-2.0:free` | SUCCESS | 5/5 complete; 5 `REVISE` |
| 2 | `nous / upstage/solar-pro4:free` | SUCCESS | 5/5 complete; 4 `REVISE`, 1 `ACCEPT` |
| 3 | `nous / stepfun/step-3.7-flash:free` | SUCCESS | 5/5 after one bounded retry; 4 `REVISE`, 1 `ACCEPT`; one transient upstream capacity event |
| 4 | `nous / inclusionai/ling-3.0-flash-fin:free` | SUCCESS | 5/5 complete; 4 `REVISE`, 1 `ACCEPT` |
| 5 | `openrouter / minimax/minimax-m3:free` | SUCCESS | 5/5 complete; 4 `REVISE`, 1 `ACCEPT` |
| 6 | `openrouter / nvidia/nemotron-3.5-lightning:free` | SUCCESS | 5/5 complete; 4 `REVISE`, 1 `ACCEPT` |
| 7 | `groq / openai/gpt-oss-120b` | runner UNKNOWN | Not run: two sentinel attempts stopped before provider response because Hermes context compression was paused |
| 8 | `opencode-go / glm-5.3-flash` | pending at checkpoint | paid pass pending |
| 9 | OpenAI subscription `Sol` | not started | must be last |

The roster is provider-stratified and bounded to distinct general-purpose free routes. Specialized aliases and duplicate family entries are recorded as not run rather than silently counted as tested.

## Non-secret evidence boundary

Only provider names, model identifiers, statuses, timings, classifications, and redaction-safe model responses belong here. OAuth values, bearer tokens, API keys, connection strings, private transcripts, and runtime databases do not belong in this repository.
