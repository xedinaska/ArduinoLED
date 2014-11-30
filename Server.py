#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
from LEDController import ArduinoLEDController

PORT_NUMBER = 8080


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/html/index.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False

            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True

            if sendReply:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(bytes(f.read(), 'utf-8'))
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    #Handler for the POST requests
    def do_POST(self):
        if self.path == "/send":

            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']}
            )

            arduinoController = ArduinoLEDController.ArduinoLEDController()
            arduinoController.handle(form["color"].value)

            self.send_response(200)
            self.end_headers()

            return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()