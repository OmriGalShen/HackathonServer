import http.server as server
import os
import sys

import algo

PORT = os.environ['PORT']
# PORT = 8000


class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """Extend SimpleHTTPRequestHandler to handle PUT requests"""

    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        filename = os.path.relpath('/app/image.jpg')
        # filename = os.path.relpath('image.jpeg')
        # filename = os.path.basename('image.jpeg')
        # print(f"path:{os.listdir('/app')}")
        # # Don't overwrite files
        # if os.path.exists(filename):
        #     self.send_response(409, 'Conflict')
        #     self.end_headers()
        #     reply_body = '"%s" already exists\n' % filename
        #     self.wfile.write(reply_body.encode('utf-8'))
        #     return

        file_length = int(self.headers['Content-Length'])
        with open(filename, 'wb') as output_file:
            output_file.write((self.rfile.read(int(self.headers['content-length']))).decode('utf-8'))
        print("BOOOM!!!")
        self.send_response(201, 'Created')
        self.end_headers()
        # reply_body = 'Saved "%s"\n' % filename
        # reply_body = 'price:2000'
        # reply_body = f"path:{os.listdir('/app/src')}"
        reply_body = algo.price_and_model()
        self.wfile.write(reply_body.encode('utf-8'))


def run(server_class=server.HTTPServer, handler_class=HTTPRequestHandler):
    server_address = ('', int(PORT))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    print("running server")
    sys.stdout.flush()
    run()



