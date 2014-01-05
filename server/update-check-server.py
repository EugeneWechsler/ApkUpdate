#!/usr/bin/python
# coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse
import sys, getopt


DEFAULT_PORT_NUMBER = 8888

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        url = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(url.query)

        self.send_response(200)
        self.send_header('Content-type','text/pain')
        self.end_headers()
        # Send the html message
        self.wfile.write(self.path)
        return

server = None
try:
    #Create a web server and define the handler to manage the
    #incoming request
    try:
        opts, args = getopt.getopt(sys.argv[1:],'p:',['port='])
    except getopt.GetoptError:
        print sys.argv[0] + ' -p <port>'
        sys.exit(2)
    port = DEFAULT_PORT_NUMBER
    print opts
    for opt, arg in opts:
        if opt in ('-p', '--port'):
            port = int(arg)

    server = HTTPServer(('', port), myHandler)
    print 'Started httpserver on port ' , port

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
