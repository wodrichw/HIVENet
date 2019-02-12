from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sys import argv
import SocketServer
import simplejson
import random
import tarfile

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print(self.data_string)
        self.send_response(200)
        self.end_headers()
        data = simplejson.loads(self.data_string)

        if self.path  == '/classifier':
            self.do_classifier(data)
        elif self.path == '/names':
            self.do_names(data)
        elif self.path == '/training-data':
            self.do_trainingData(data)
            
    
    def do_classifier(self, data):
        with open("../classifier.pkl", "w") as outfile:
            simplejson.dump(data, outfile)
        return

    def do_names(self, data):
        with open("../real-time-deep-face-recognition/names.txt", "a") as outfile:
            simplejson.dump(data, outfile)
        return

    def do_trainingData(self, data):
        name = data['name']
        archive = data['archive']
        archiveName = "../datasets/data/" + name + "tar.gz"
        with open(archiveName, 'w') as outfile:
            simplejson.dump(archive, outfile)
        tarfile.TarFile.extractall(archiveName)

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("127.0.0.1", port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
