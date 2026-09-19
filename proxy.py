#!/usr/bin/env python3
import http.server, socketserver, urllib.request, urllib.error, json, os, sys

# OpenAI-compatible upstream. Override any of these with env vars; never
# hardcode the key here — this file is committed.
UPSTREAM = os.environ.get("CODECRAFT_URL", "https://codecraftapi.com/v1/chat/completions")
MODEL    = os.environ.get("CODECRAFT_MODEL", "deepseek-v4-flash-0731")
API_KEY  = os.environ.get("CODECRAFT_KEY") or os.environ.get("BROCODE_KEY", "")
PORT     = int(os.environ.get("PROXY_PORT", "8787"))
SYSTEM   = os.environ.get(
    "CODECRAFT_SYSTEM",
    "You are the terminal on Bhushan Sahane's engineering portfolio. He is a "
    "Senior System Administrator at Red Hat with ~9 years of infrastructure "
    "experience, RHCE and RHCSA certified, working on MCP servers, RAG "
    "pipelines and agentic AI. Answer in under 60 words, plain text, no "
    "markdown. If you do not know something about him, say so plainly and "
    "suggest emailing sahane.bhushan7@gmail.com."
)

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
        "upstream": UPSTREAM,
        "model": MODEL
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
        "error": "CODECRAFT_KEY not configured on proxy. Local knowledge engine active."
      }).encode())
      return

    n = int(self.headers.get("Content-Length", 0))
    body = self.rfile.read(n) if n else b""

    # The page sends {messages:[...]}; the model and system prompt are the
    # proxy's business, so a browser can never select a costlier model.
    try:
      incoming = json.loads(body or b"{}")
    except ValueError:
      incoming = {}
    msgs = [m for m in incoming.get("messages", []) if m.get("role") in ("user", "assistant")]
    payload = {
      "model": MODEL,
      "max_tokens": int(incoming.get("max_tokens") or 300),
      "messages": [{"role": "system", "content": SYSTEM}] + msgs[-8:],
    }

    req = urllib.request.Request(
      UPSTREAM, data=json.dumps(payload).encode(), method="POST",
      headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY,
        # urllib's default UA is blocked outright by the upstream's CDN (403
        # before the request ever reaches the origin). Identify properly.
        "User-Agent": "bsahane-portfolio-proxy/1.0",
        "Accept": "application/json",
      },
    )
    try:
      with urllib.request.urlopen(req, timeout=20) as r:
        raw = json.loads(r.read())
      # Normalise OpenAI shape to the one the page already reads, so the
      # browser stays protocol-agnostic.
      text = ""
      try:
        text = raw["choices"][0]["message"]["content"]
      except (KeyError, IndexError, TypeError):
        pass
      self.send_response(200 if text else 502)
      self.send_header("Content-Type", "application/json")
      self._cors()
      self.end_headers()
      self.wfile.write(json.dumps(
        {"content": [{"type": "text", "text": text}], "model": MODEL}
        if text else {"error": "empty completion"}
      ).encode())
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
