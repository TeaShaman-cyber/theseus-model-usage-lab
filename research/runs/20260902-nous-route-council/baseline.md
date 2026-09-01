# Parent baseline — Nous route council experiment

- experiment: `ISSUE-20260901-NOUS-ROUTE-COUNCIL-EXPERIMENT`
- stage: baseline-before-council
- captured: 2026-09-01
- parent_verdict: `NEEDS_TWO_LANES`
- confidence: 0.78

## Proposed minimum design

1. Separate client/TLS observation from provider/model verdict.
2. Use Windows `curl.exe`/Schannel as primary direct probe; keep Python `urllib` only as labeled comparison control.
3. Require bounded semantic `/chat/completions` with `max_tokens >= 200`, non-empty content, and parsed body.
4. Treat `/models` as catalog evidence only.
5. Emit machine-readable classifications for client fingerprint block, authentication, plan gate, model unavailable, overload, timeout, proxy transport, malformed/embedded error, and success.
6. Prefer Hermes proxy for credential ownership; never print or copy OAuth bearer values. Use Hindsight LLM trace/read-only health only as a separate postcondition, not proof of direct upstream health.

## Facts used

- Prior experiment observed Python `urllib` Cloudflare 1010 while curl from the same egress passed.
- A successful Hindsight/Solar trace exists, so a direct 403 probe is not enough to declare Solar unavailable.
- Hermes delegation has one global provider/model pin; route rotation requires read-back and restoration.

## Assumptions

- `curl.exe` is available on the Windows host and uses a materially different TLS stack from Python in this environment.
- A safe diagnostic can exercise the proxy without exposing its OAuth state.

## Weakest point

The baseline does not yet prove how to perform a direct upstream chat probe without temporarily handling a credential outside Hermes proxy. A correct tool may therefore need separate direct-client and proxy-route modes.

## What would change my mind

A council or live control showing the client distinction is not reproducible, or that a simpler single-lane proxy probe yields the same verified diagnostic coverage without losing TLS-fingerprint classification.
