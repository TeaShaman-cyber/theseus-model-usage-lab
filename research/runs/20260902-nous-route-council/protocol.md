# Council protocol

## Fixed task

Assess the design of a read-only CLI diagnostic for the Hermes/Nous route. The tool must distinguish client/TLS fingerprint blocks, credential failures, proxy reachability, provider/upstream overload, model unavailability, timeouts, embedded errors, and success without declaring a model dead from one HTTP status.

## Independent masks

Each executor route receives the same packet independently:

- `ARCHIVIST`: chronology, provenance, freshness, reproducibility;
- `PRACTITIONER`: safe day-to-day operation, budgets, next action, restore safety;
- `SYSTEMS_ENGINEER`: layers, schemas, precedence, fixtures, testability;
- `NEWCOMER`: first-run comprehension and operator safety;
- `SKEPTIC`: falsification, abstention, ambiguity, correlated error.

No mask receives the parent baseline or another mask's result. Each response uses the same machine schema: `mask`, `verdict`, `confidence`, `reasoning`, `facts`, `assumptions`, `unique_findings`, `what_would_change_my_mind`, `weakest_point`.

## Evidence packet

The packet records the verified urllib-vs-curl/Schannel 1010 differential, historical successful chat calls, the direct-probe-vs-Hindsight conflict, Hermes-owned OAuth refresh, `/models` as catalog-only, `/chat/completions` with `max_tokens >= 200`, parsed JSON/SSE/HTML bodies, global-pin rotation and restore requirements, and read-only Hindsight postconditions.

## Staging and validity

1. Sentinel before every executor route.
2. Free provider routes first; paid `opencode-go` next; OpenAI Sol last.
3. A literal packet truncation invalidates a content pass.
4. A non-streaming timeout is recorded as delivery/latency evidence; partial JSON is not silently promoted to a normal completed pass.
5. Provider capacity, runner failure, and model failure are separate labels.
6. No runtime mutation, Hindsight retain, credential output, or operational decision follows from a council response without live verification.

## Redaction

Credentials, bearer values, OAuth state, connection strings, local runtime paths, and raw live transcripts are excluded. Research artifacts contain only redaction-safe structured outputs and event metadata.
