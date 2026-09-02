# Nous-route diagnostic sandbox

Purpose: give implementation subagents real hands for a bounded test run without
letting them touch the operational repository, Hermes runtime, Hindsight, OAuth
state, or the public Nous route.

## Capability contract

```yaml
filesystem: isolated_sandbox_worktree_only
network: internal_compose_network_only
internet: forbidden_at_runtime
Docker: ephemeral_compose_wrapper_only
host_mounts: none
host_docker_socket: forbidden
secrets: none
Hindsight: no_read_no_write
external_writes: forbidden
promotion: parent_diff_review_then_explicit_user_approval
```

The compose project contains two deterministic HTTP fixtures (`nous-stub` and
`proxy-stub`) and one test runner. The network is Compose-internal and marked
`internal: true`; no service can reach the public internet. The fake services
never read credentials and never write shared state.

## Covered response fixtures

- normal chat completion with `max_tokens >= 200`;
- request rejected when `max_tokens < 200`;
- HTTP 200 with an embedded provider error;
- structured 401 authentication error;
- structured 404 model-not-found error;
- structured 429 upstream-overload error;
- HTML Cloudflare-style 1010 and 1020 responses;
- malformed non-JSON body;
- fragmented SSE containing an embedded error;
- bounded timeout;
- `/models` catalog response versus `/chat/completions` liveness;
- `/v1/chat/completions` through the proxy-shaped fixture path.

## Run

From this directory:

```text
docker compose -p theseus-council-sandbox config --quiet
docker compose -p theseus-council-sandbox up --build --abort-on-container-exit --exit-code-from test-runner
```

The expected postcondition is `sandbox tests passed` and exit code `0`.

The base image is intentionally a normal public Python image for this first
pilot. Before durable CI use, capture and pin its digest. The sandbox itself is
not a production or recovery stack and must not be added to automatic startup.

## Worker workflow

A builder child may write code and run tests only inside its isolated worktree
against these fixtures. It must return:

- changed-file list;
- diff or patch proposal;
- exact test command and exit code;
- sanitized test output;
- known limitations.

The parent verifies the diff and postconditions. No child promotes files into
`theseus-local-lab`; promotion remains a separate user-approved mutation.
