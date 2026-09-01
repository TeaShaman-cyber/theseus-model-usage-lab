# Free-route inventory

Captured: 2026-09-02
Scope: bounded provider-stratified general-purpose free routes. The catalog is not treated as proof of availability; each included route passed a no-tool sentinel before a council batch.

| Provider | Exact model | Sentinel | Council |
|---|---|---:|---:|
| nous | `meituan/longcat-2.0:free` | SUCCESS | 5/5 |
| nous | `upstage/solar-pro4:free` | SUCCESS | 5/5 |
| nous | `stepfun/step-3.7-flash:free` | SUCCESS | 5/5; one bounded executor-capacity retry |
| nous | `inclusionai/ling-3.0-flash-fin:free` | SUCCESS | 5/5 |
| openrouter | `minimax/minimax-m3:free` | SUCCESS | 5/5 |
| openrouter | `nvidia/nemotron-3.5-lightning:free` | SUCCESS | 5/5 |
| groq | `openai/gpt-oss-120b` | UNKNOWN_RUNNER | not run; two sentinel attempts ended in Hermes context-compression failure before provider response |

## Interpretation

This is a bounded live roster, not a claim that every free catalog entry was tested. Duplicate aliases and specialized candidates were not silently counted; they remain outside this run until an identity map and a separate budget are approved. `UNKNOWN_RUNNER` is neither model failure nor provider failure.
