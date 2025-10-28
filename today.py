from http.server import BaseHTTPRequestHandler
import json
from datetime import date

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        
        response = {"today": date.today().isoformat()}
        self.wfile.write(json.dumps(response).encode())
