#!/usr/bin/env python3
import json
import os
import socket
import urllib.error
import urllib.request


NOUS = os.environ["NOUS_STUB_URL"]
PROXY = os.environ["PROXY_STUB_URL"]


def call(base, path, scenario="success", max_tokens=200, timeout=2):
    payload = {"model": "fixture-model", "messages": [{"role": "user", "content": "fixture"}], "max_tokens": max_tokens}
    request = urllib.request.Request(
        base + path + "?scenario=" + scenario,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer [REDACTED]"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.headers.get("Content-Type", ""), response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        return error.code, error.headers.get("Content-Type", ""), error.read().decode("utf-8")


def assert_json(text):
    return json.loads(text)


def main():
    checks = []

    status, content_type, body = call(NOUS, "/chat/completions")
    data = assert_json(body)
    assert status == 200 and data["choices"][0]["message"]["content"] == "SANDBOX_OK"
    checks.append("success")

    status, _, body = call(NOUS, "/chat/completions", max_tokens=199)
    assert status == 400 and assert_json(body)["error"]["type"] == "invalid_request_error"
    checks.append("max_tokens_floor")

    status, _, body = call(NOUS, "/chat/completions", "embedded_error")
    assert status == 200 and assert_json(body)["error"]["type"] == "upstream_overload"
    checks.append("http_200_embedded_error")

    for scenario, expected_status, expected_type in [
        ("auth_failure", 401, "authentication_error"),
        ("model_not_found", 404, "model_not_found"),
        ("upstream_overload", 429, "rate_limit_error"),
    ]:
        status, _, body = call(NOUS, "/chat/completions", scenario)
        assert status == expected_status and assert_json(body)["error"]["type"] == expected_type
        checks.append(scenario)

    status, content_type, body = call(NOUS, "/chat/completions", "html_1010")
    assert status == 403 and content_type.startswith("text/html") and "1010" in body
    checks.append("html_1010")

    status, content_type, body = call(NOUS, "/chat/completions", "html_1020")
    assert status == 403 and content_type.startswith("text/html") and "1020" in body
    checks.append("html_1020")

    status, content_type, body = call(NOUS, "/chat/completions", "malformed")
    assert status == 200 and content_type.startswith("text/plain") and body == "not-json-fixture"
    checks.append("malformed_body")

    status, content_type, body = call(NOUS, "/chat/completions", "sse_error")
    assert status == 200 and content_type.startswith("text/event-stream") and '"type":"upstream_overload"' in body
    checks.append("sse_embedded_error")

    try:
        call(NOUS, "/chat/completions", "timeout", timeout=0.1)
    except (TimeoutError, socket.timeout, urllib.error.URLError):
        checks.append("timeout")
    else:
        raise AssertionError("timeout fixture did not time out")

    status, _, body = call(PROXY, "/chat/completions")
    data = assert_json(body)
    assert status == 200 and data["fixture_role"] == "proxy"
    checks.append("proxy_shaped_route")

    with urllib.request.urlopen(NOUS + "/models", timeout=2) as response:
        catalog = json.loads(response.read().decode("utf-8"))
    assert response.status == 200 and catalog["data"][0]["id"] == "fixture-model"
    checks.append("catalog_only")

    print(json.dumps({"sandbox": "nous-route-diagnostic", "checks": checks, "count": len(checks)}))
    print("sandbox tests passed")


if __name__ == "__main__":
    main()
