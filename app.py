from http.server import BaseHTTPRequestHandler, HTTPServer
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Возвращаем простой HTTP-ответ
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello World!\n")
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 32777
    server = HTTPServer((host, port), HelloHandler)
    print(f"Server started on http://{host}:{port}")
    server.serve_forever()
