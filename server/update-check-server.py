#!/usr/bin/python
# coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse
import sys, getopt
import packages
import settings
import os


DEFAULT_PORT_NUMBER = 8888

def binaryPath(package, version, variant):
    return os.path.join(packages.packagesPath,package,repr(version),variant+'.apk')

def readBinary(path):
    f = open(path)
    data = f.read()
    f.close()
    return data


#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        url = urlparse.urlparse(self.path)
        print url
        if url.path == '/check':
            params = dict(urlparse.parse_qsl(url.query))
            packageName = params.get('package_name')
            version = int(params.get('version', -1))
            variantId = params.get('variant_id','')

            # md5 = params['md5']
            if not packageName:
                self.send_response(404)
                return

            self.send_response(200)
            self.send_header('content-type','text/plain')
            self.end_headers()

            packageVersions = packages.packages.get(packageName)
            if packageVersions:
                lastVersion=packageVersions.get(variantId, -1)
                if lastVersion > version:
                    downloadLink = urlparse.urljoin(settings.downloadHostUrl,
                                                    'get?package_name=%s&variant_id=%s' % (packageName, variantId))
                    self.wfile.write('have update\n')
                    self.wfile.write(downloadLink)
                    return
            self.wfile.writeln('no update')

        elif url.path == '/get':
            params = dict(urlparse.parse_qsl(url.query))
            packageName = params.get('package_name')
            package = binaries.get(packageName)
            if package:
                binary = package[params.get('variant_id','')]
            else:
                binary = None

            if binary:
                self.send_response(200)
                self.send_header('content-type','application/vnd.android.package-archive')
                self.end_headers()
                self.wfile.write(binary)
            else:
                self.send_response(400)
        else:
            self.send_response(404)

def loadBinariesForPackage(package):
    variants = packages.packages[package]
    return dict([(c, readBinary(binaryPath(package,v, c))) for c,v in variants.items()])

binaries = dict([(k,loadBinariesForPackage(k))
                            for k in packages.packages.keys()])

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
