#!/usr/bin/env python3
import http.server, socketserver, urllib.request, urllib.error, json, os, sys

UPSTREAM = "https://api.brocode.live/v1/messages"
API_KEY = os.environ.get("BROCODE_KEY", "")
PORT = int(os.environ.get("PROXY_PORT", "8787"))

CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
  "Access-Control-Max-Age": "86400",
}

class Handler(http.server.BaseHTTPRequestHandler):
  def log_message(self, fmt, *a):
    sys.stderr.write("[proxy] " + (fmt % a) + "\n")

  def _cors(self):
    for k, v in CORS.items():
      self.send_header(k, v)

  def do_OPTIONS(self):
    self.send_response(204)
    self.send_header("Content-Length", "0")
    self._cors()
    self.end_headers()

  def do_GET(self):
    if self.path == "/health" or self.path == "/":
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      status_data = {
        "status": "healthy",
        "service": "bsahane-terminal-proxy",
        "has_key": bool(API_KEY),
        "upstream": UPSTREAM
      }
      self.wfile.write(json.dumps(status_data).encode())
      return

    self.send_response(404)
    self.send_header("Content-Type", "application/json")
    self._cors()
    self.end_headers()
    self.wfile.write(json.dumps({"error": "Not found"}).encode())

  def do_POST(self):
    if not API_KEY:
      self.send_response(503)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      self.wfile.write(json.dumps({
        "error": "BROCODE_KEY not configured on proxy. Local knowledge engine active."
      }).encode())
      return

    n = int(self.headers.get("Content-Length", 0))
    body = self.rfile.read(n) if n else b""
    req = urllib.request.Request(
      UPSTREAM, data=body, method="POST",
      headers={
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "anthropic-dangerous-direct-browser-access": "true",
      },
    )
    try:
      with urllib.request.urlopen(req, timeout=120) as r:
        out = r.read()
      self.send_response(r.status)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      self.wfile.write(out)
    except urllib.error.HTTPError as e:
      self.send_response(e.code)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      self.wfile.write(json.dumps({"error": str(e.reason)}).encode())
    except urllib.error.URLError as e:
      self.send_response(502)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      self.wfile.write(json.dumps({"error": str(e.reason)}).encode())

class ThreadedServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
  allow_reuse_address = True
  daemon_threads = True

if __name__ == "__main__":
  print(f"[proxy] http://127.0.0.1:{PORT} -> {UPSTREAM}")
  try:
    ThreadedServer(("127.0.0.1", PORT), Handler).serve_forever()
  except KeyboardInterrupt:
    print("\n[proxy] stopped")
