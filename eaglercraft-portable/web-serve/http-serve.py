#!/usr/bin/env python3
import http.server
import socketserver
import mimetypes
import sys
from pathlib import Path

# ---- CONFIG ----
PORT = 8080
ROOT_DIR = Path(".")  # serve current directory
# ----------------

# REQUIRED: proper WASM MIME
mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("application/javascript", ".js")

class EaglerHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files strictly from ROOT_DIR
        path = path.split("?", 1)[0].split("#", 1)[0]
        rel = Path(path.lstrip("/"))
        full = (ROOT_DIR / rel).resolve()

        # Prevent directory traversal
        if not str(full).startswith(str(ROOT_DIR.resolve())):
            return str(ROOT_DIR / "index.html")

        if full.is_dir():
            return str(full / "index.html")

        return str(full)

    def log_message(self, fmt, *args):
        # Silence spam (optional)
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])

    with socketserver.TCPServer(("0.0.0.0", PORT), EaglerHandler) as httpd:
        print(f"[+] Serving Eagler client on http://0.0.0.0:{PORT}")
        httpd.serve_forever()
