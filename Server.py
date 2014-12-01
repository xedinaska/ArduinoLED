#!/usr/bin/python
from http.server import HTTPServer
from HTTPHandler import HTTPArduinoLEDHandler

PORT_NUMBER = 8080


try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), HTTPArduinoLEDHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()