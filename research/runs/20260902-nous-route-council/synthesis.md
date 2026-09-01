# Nous-route council experiment — synthesis

- experiment: `ISSUE-20260901-NOUS-ROUTE-COUNCIL-EXPERIMENT`
- issue: https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/7
- run: `20260902-nous-route-council`
- captured: 2026-09-02
- operational mutation: none

## Verified run totals

The same fixed packet and five masks were used for every normal pass. The
structured artifact contains 40 records:

- 35 normal-valid responses: 7 passes x 5 masks;
- 4 `partial_timeout` paid responses from `opencode-go`;
- 1 additional `partial_timeout` Skeptic retry from `opencode-go` is included
  as a separate delivery event;
- the two earlier `opencode-go` attempts with literal brief truncation and
  non-streaming timeout are not counted as normal council passes;
- Groq `openai/gpt-oss-120b` was not run because two sentinels failed in the
  Hermes runner before any provider response;
- no credential value, bearer, OAuth state, live transcript, or Hindsight
  write was collected.

Normal-valid verdict totals (computed from `responses.jsonl`):

- `REVISE`: 30/35;
- `ACCEPT`: 5/35;
- `REJECT`: 0/35.

Every normal-valid pass had a majority `REVISE` verdict:

| Pass | Provider / model | Delivery | Verdicts |
|---:|---|---|---|
| 1 | Nous / `meituan/longcat-2.0:free` | 5/5 valid | 5 REVISE |
| 2 | Nous / `upstage/solar-pro4:free` | 5/5 valid | 4 REVISE, 1 ACCEPT |
| 3 | Nous / `stepfun/step-3.7-flash:free` | 5/5 valid after one bounded Practitioner retry | 4 REVISE, 1 ACCEPT |
| 4 | Nous / `inclusionai/ling-3.0-flash-fin:free` | 5/5 valid | 4 REVISE, 1 ACCEPT |
| 5 | OpenRouter / `minimax/minimax-m3:free` | 5/5 valid | 4 REVISE, 1 ACCEPT |
| 6 | OpenRouter / `nvidia/nemotron-3.5-lightning:free` | 5/5 valid | 4 REVISE, 1 ACCEPT |
| 7 | Groq / `openai/gpt-oss-120b` | runner blocked | not run |
| 8c/8d | OpenCode / `glm-5.3-flash` | partial timeout / delivery failures | excluded from normal-valid totals |
| 9 | OpenAI Codex / `gpt-5.6-sol-900k` (Sol) | 5/5 valid | 5 REVISE |

## Baseline comparison

The parent baseline was `NEEDS_TWO_LANES`: separate the curl/Schannel
client observation from the provider/model verdict, require a semantic chat
probe, and keep Hindsight as a separate read-only postcondition.

The council did not overturn that baseline. It made the acceptance bar more
specific. The most stable additions across model families were:

1. observations must be layer- and transport-scoped; curl success and urllib
   `CLIENT_TLS_FINGERPRINT_BLOCK` may coexist instead of overwriting each other;
2. `INDETERMINATE` must be a first-class outcome for conflicting, insufficient,
   or provenance-unknown evidence;
3. `/chat/completions` with `max_tokens >= 200` and body parsing is the liveness
   test; `/models` remains catalog-only;
4. JSON, fragmented SSE, HTML/interstitial, malformed, and HTTP-200 embedded
   error bodies need explicit parser and fixture paths;
5. the global pin must default to non-mutating diagnostics; any rotation needs
   an explicit mode, exclusive ownership, durable journal, revision/CAS check,
   startup recovery, and verified restoration;
6. every terminal finding needs numeric budget, freshness, stable exit code,
   and one allowed next action.

The council therefore answers the practical question as: **yes, it materially
improved the design review over the parent baseline, but the design remains
`REVISE` and is not an implementation approval.**

## What the council added versus repetition

### Replicated signals, not new proof

All seven valid model routes repeatedly rejected the dangerous shortcuts that
were already in the packet: a single HTTP status is not provider death,
Cloudflare 1010 can be client/TLS-sensitive, `/models` is not liveness, and
HTTP 200 requires body inspection. This is cross-model replication, not
independent proof of those historical facts.

### Cross-pass additions with operational value

The following findings appeared with different wording and complementary
emphasis across the masks and providers:

- **Temporal/provenance:** define freshness TTLs, UTC event epochs, client
  versions, egress identity, endpoint/payload identity, parser version, and
  immutable fixture IDs.
- **Safe mutation:** separate read-only default mode from explicitly acknowledged
  rotation; use a lock/lease, durable journal, startup recovery, compare-and-
  swap restoration, and `RESTORE_CONFLICT` rather than blind overwrite.
- **Classification:** preserve multi-label observations and aggregate verdicts
  separately; define deterministic precedence for transport, auth, model,
  overload, body, and ambiguity cases.
- **Operator contract:** publish a quick start, exact commands, visible call and
  token budgets, retry/deadline values, stable exit codes, plain-language next
  steps, and explicit non-conclusions.
- **Parser boundary:** fixture-test JSON, fragmented SSE, HTML/WAF pages,
  malformed bodies, and HTTP-200 embedded errors before assigning a provider or
  model finding.
- **Artifact isolation:** keep probe bodies and headers out of Hindsight,
  shared logs, Git, and credentials; store only bounded redacted snippets or
  digests.

## Robustness and bias observations

- Role diversity produced useful disagreement: in passes 2–6 one role accepted
  the skeleton while four required revision. That is more informative than a
  false unanimous vote and demonstrates role-level coverage.
- Model-family diversity did not create a provider-specific reversal: the
  normal-valid majority was `REVISE` for all seven passes, including Sol.
- Sol contributed the clearest explicit contract around leases, journals, CAS,
  startup recovery, numeric budgets, and observation-scoped findings. This is an
  observed contribution, not proof that the model is intrinsically superior.
- `opencode-go / glm-5.3-flash` exposed a different risk: repeated long
  non-streaming latency and partial delivery under a five-mask fan-out. That is
  a route/runner observation and must not be interpreted as a design verdict.
- Groq could not be compared because the runner failed before provider
  execution. It remains `UNKNOWN_RUNNER`, not model failure.

## Limits

- The packet supplied the historical facts and desired taxonomy, so repeated
  detection of those facts is not a blind discovery benchmark.
- No live diagnostic implementation was built or exercised in this run; model
  recommendations remain hypotheses until verified against `theseus-local-lab#4`
  and live route/Hindsight postconditions.
- The research clone is disposable because `theseus-model-usage-lab` is not yet
  registered as a canonical local workspace in the Theseus workspace registry.
  The remote repository and issue are real; canonical-path registration is a
  separate scope decision.
- Hermes summary artifacts may contain bounded text excerpts; private live
  transcripts remain outside the repository.

## Research verdict

**Council result: ACCEPT the direction, REVISE the design.**

The council helped by converting a correct but abstract two-lane baseline into
an implementation gate with explicit temporal, transactional, parser,
operator, and artifact-safety requirements. It did not justify changing the
Nous runtime, choosing a new Hindsight route, or declaring any provider/model
healthy or dead. Those remain live-verification tasks for the separate
operational issue.
