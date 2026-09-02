#!/usr/bin/env python3
import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class FixtureHandler(BaseHTTPRequestHandler):
    server_version = "TheseusFixture/1.0"

    def _route(self):
        path = urlparse(self.path)
        route = path.path
        if route.startswith("/v1"):
            route = route[3:] or "/"
        return route, parse_qs(path.query)

    def _send_json(self, status, payload):
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, status, content_type, body):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        route, _ = self._route()
        if route == "/health":
            self._send_json(200, {"status": "ok", "role": self.server.role})
        elif route == "/models":
            self._send_json(200, {"object": "list", "data": [{"id": "fixture-model"}]})
        else:
            self._send_json(404, {"error": {"type": "not_found", "message": "fixture route not found"}})

    def do_POST(self):
        route, query = self._route()
        if route != "/chat/completions":
            self._send_json(404, {"error": {"type": "not_found", "message": "fixture route not found"}})
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            request = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"error": {"type": "invalid_json", "message": "fixture request is not JSON"}})
            return

        if int(request.get("max_tokens", 0)) < 200:
            self._send_json(400, {"error": {"type": "invalid_request_error", "message": "max_tokens must be >= 200"}})
            return

        scenario = query.get("scenario", ["success"])[0]
        if scenario == "success":
            self._send_json(200, {
                "id": "fixture-completion",
                "choices": [{"message": {"role": "assistant", "content": "SANDBOX_OK"}}],
                "fixture_role": self.server.role,
            })
        elif scenario == "embedded_error":
            self._send_json(200, {"error": {"type": "upstream_overload", "message": "embedded fixture error"}})
        elif scenario == "auth_failure":
            self._send_json(401, {"error": {"type": "authentication_error", "message": "fixture auth failure"}})
        elif scenario == "model_not_found":
            self._send_json(404, {"error": {"type": "model_not_found", "message": "fixture-model unavailable"}})
        elif scenario == "upstream_overload":
            self._send_json(429, {"error": {"type": "rate_limit_error", "message": "fixture upstream overload", "retryable": True}})
        elif scenario == "html_1010":
            self._send_text(403, "text/html", "<html><body>Cloudflare error code: 1010</body></html>")
        elif scenario == "html_1020":
            self._send_text(403, "text/html", "<html><body>Cloudflare error code: 1020</body></html>")
        elif scenario == "malformed":
            self._send_text(200, "text/plain", "not-json-fixture")
        elif scenario == "sse_error":
            chunks = [
                'data: {"id":"fixture","choices":[{"delta":{"content":"partial"}}]}\n\n',
                'data: {"error":{"type":"upstream_overload","message":"sse fixture error"}}\n\n',
                "data: [DONE]\n\n",
            ]
            body = "".join(chunks).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif scenario == "timeout":
            time.sleep(5)
            self._send_json(200, {"choices": []})
        else:
            self._send_json(400, {"error": {"type": "unknown_fixture", "message": scenario}})

    def log_message(self, format_string, *args):
        print("fixture: " + format_string % args, flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--role", required=True)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("0.0.0.0", args.port), FixtureHandler)
    server.role = args.role
    print(json.dumps({"fixture_server": args.role, "port": args.port}), flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
