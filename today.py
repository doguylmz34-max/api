from http.server import BaseHTTPRequestHandler
import json
from datetime import date

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"today": date.today().isoformat()}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
