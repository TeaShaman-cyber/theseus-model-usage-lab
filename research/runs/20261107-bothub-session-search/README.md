# BotHub RUB economics × Session Search translation — 2026-11-07

Issue: https://github.com/TeaShaman-cyber/theseus-model-usage-lab/issues/17  
Quality owner: https://github.com/TeaShaman-cyber/theseus-session-search-lab/issues/176  
exe.dev integration receipt: https://github.com/TeaShaman-cyber/theseus-research/issues/112

This run characterizes BotHub billing/usage observability for a bounded real
workload. It does **not** own the Session Search quality conclusion.

## Frozen execution evidence

Session Search frozen authority:
- gold rows: 20;
- cases: 10;
- `gold_digest_v2 = 5c1e817960a3e8222ec9cdba6f9ec135b5c00d6e7be0f42a2dbf50775956a6d7`.

Live windows:
- run A: `2026-11-07T13:10:44Z..13:11:54Z`;
- run B: `2026-11-07T13:13:40Z..13:14:40Z`.

Provider-account reconciliation window:
`2026-11-07T13:08:13Z..13:15:10Z`.

The wider accounting window intentionally includes the two first successful
BotHub calls that were rejected locally only because the initial runner expected
unprefixed response model IDs.

## FACT — BotHub provider report

`GET /api/v2/transaction/usage-report` returned HTTP 200 and exactly 32 rows
inside the accounting window. All 32 matched the three benchmark models.

| model_id | requests | provider | prompt | completion | cached | CAPS |
|---|---:|---|---:|---:|---:|---:|
| `gemini-2.5-flash-lite` | 10 | Google/Gemini | 800 | 3639 | 0 | 1074.988927 |
| `gpt-4.1-nano` | 11 | OpenRouter | 998 | 225 | 0 | 132.868519 |
| `deepseek-v4.1-flash` | 11 | OpenRouter | 1233 | 1919 | 0 | 805.720862 |

Total provider-report spend: **2013.578308 CAPS**.

The 11th GPT and DeepSeek calls are the initial canonical-ID guard failures.
They received successful provider responses and therefore correctly appear as
billable transactions.

## FACT — account delta

A private pre/post `GET /api/v2/auth/me` snapshot was taken locally on the
authorized laptop. Raw balances and account fields were not committed.

Observed during the reconciliation window:
- `subscription.balance` delta: **-2029**;
- `subscription.availableBalance` delta: **-2029**;
- plan currency field: `RUB`.

The provider report accounts for 2013.578308 of the 2029-unit balance decrease.
Residual: **15.421692 units**, approximately **0.760%** of the observed account
delta.

The exact cause of that residual is **UNKNOWN**. Do not call it rounding,
settlement, tax, markup or unrelated spend without new evidence.

## FACT — BotHub units are not one field

BotHub's current public model catalog describes **CAPS as the service's internal
currency**. The developer surface separately exposes RUB-denominated model
prices and an API-key provider mode choice (ECO / PRO).

Therefore:
- account `balance` / `availableBalance` and usage-report `CAPS` are
  internal accounting units;
- `plan.currency=RUB` does not establish that a numeric balance delta is RUB;
- public RUB tariff and CAPS report must remain separate evidence streams until
  the conversion/routing contract is established.

Current provider mode for the key used in this run is **UNKNOWN**. It was not
read back from an authoritative API surface.

## Public RUB tariff snapshot — estimate only

Snapshot recorded before inference from BotHub's public model catalog:

| model | input RUB / 1M | output RUB / 1M |
|---|---:|---:|
| Gemini 2.5 Flash Lite | 4.38 | 17.53 |
| GPT-4.1 Nano | 4.38 | 17.53 |
| DeepSeek V4.1 Flash | 4.25 | 47.21 |

Applying those rates mechanically to the 32 usage-report rows gives:

| model | estimated RUB |
|---|---:|
| Gemini 2.5 Flash Lite | 0.06729567 |
| GPT-4.1 Nano | 0.00831549 |
| DeepSeek V4.1 Flash | 0.09583624 |
| **total** | **0.17144740** |

The 30 successful benchmark-arm calls alone estimate to approximately
**0.16639117 RUB**.

These figures are **INFERENCE**, not observed billing. The actual usage report
shows different provider routes (Google/Gemini vs OpenRouter), and BotHub's
ECO/PRO mode was not independently recovered. No CAPS→RUB conversion is
asserted.

Public source:
https://bothub.chat/ru/models?type=text

## FACT — response-side billing metadata is insufficient alone

For the successful benchmark arms:
- Gemini responses returned `usage.cost = null`;
- GPT-4.1 Nano and DeepSeek V4.1 Flash returned numeric `usage.cost` values;
- the unit/contract of those numeric values was not established in this run.

Therefore response `usage.cost` is not accepted as canonical billing evidence.

## Grafana / Local Lab cross-check

The expected historical Loki stream exists:

`{service_name="hindsight",log_type="llm_usage",job="hindsight-llm-requests"}`

but:
- the last 24h query returned **NO_SIGNAL**;
- a 7d query confirmed the stream and historical token/call records;
- the most recent sampled rows were unrelated Hindsight traffic
  (`upstage/solar-mini4:free`).

Thus Grafana was not fresh enough to attribute this exe.dev benchmark. The
direct BotHub usage report became the independent provider-side evidence.

This also exposes documentation drift in current `local-lab`: the old
`tools/hindsight_usage/README.md` still says BotHub has no balance/usage API,
while the newer provider-cost telemetry reference correctly records
`/api/v2/auth/me` and `/api/v2/transaction/usage-report`.

## Disposition

FACT:
- BotHub inference through exe.dev is observable by exact model and provider
  through the provider usage report.
- 32/32 calls in the bounded window were attributed.
- token totals reconcile exactly with the successful benchmark receipts plus
  the two initial guard-failure calls.
- account delta and usage-report CAPS are close but not identical.

INFERENCE:
- the workload is likely extremely cheap in RUB terms under the public tariff,
  but the public tariff is not yet reconciled to the internal CAPS ledger.

UNKNOWN:
- exact CAPS↔RUB mapping;
- key provider mode (ECO/PRO);
- cause of the 15.421692-unit reconciliation residual;
- unit/meaning of response `usage.cost` where populated.

Final disposition:

`BOTHUB_PROVIDER_USAGE_VERIFIED / MODEL_ATTRIBUTION_VERIFIED /
CAPS_LEDGER_OBSERVED / RUB_ESTIMATE_NON_AUTHORITATIVE /
ECO_PRO_UNKNOWN / GRAFANA_CURRENT_WINDOW_NO_SIGNAL /
BILLING_RECONCILIATION_PARTIAL`.
