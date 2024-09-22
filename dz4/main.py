from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import BaseServer
import urllib.parse
import mimetypes, pathlib
import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 5000
MESSAGE = None


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        print(mt, mt[0])
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        data_parse = urllib.parse.unquote_plus(data.decode())
        print(data_parse)

        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        print(data_dict)
        
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()
        run_client(UDP_IP, UDP_PORT, data_dict)

def run_client(ip, port, message):
    print(f'Connecting to server: {ip}:{port}')
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (ip, port)
    line = str(message)
    data = line.encode()
    sock.sendto(data, server)
    print(f'Send data: {message} to server: {server}')
    sock.close()


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()

