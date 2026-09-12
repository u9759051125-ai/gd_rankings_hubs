import http.server
import socketserver
import os

PORT = 9000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server avviato su http://localhost:{PORT}")
    print("Premi STOP in Pydroid per fermare il server.")
    httpd.serve_forever()
