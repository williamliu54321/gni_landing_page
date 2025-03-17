from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8000

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.css'):
            content_type = "text/css"
            file_to_open = self.path[1:]
        else:
            content_type = "text/html"
            file_to_open = 'index.html'
            
        self.send_response(200)
        self.send_header("Content-type", content_type) 
        self.end_headers()
        
        with open(file_to_open, 'rb') as file:
            self.wfile.write(file.read())

# Create and start the server
server = HTTPServer((HOST, PORT), NeuralHTTP)
print(f"Server is running on {HOST}:{PORT}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
print("Server closed")
