#!/usr/bin/python
# coding=utf-8
import urlparse
from tornado import web
import packages
import settings
import os
import tornado.ioloop
import tornado.web



DEFAULT_PORT_NUMBER = 8888

def binaryPath(package, variant):
    return os.path.join(packages.packagesPath,package,repr(variant['version']),variant['fileName'])

def readBinary(path):
    f = open(path)
    data = f.read()
    f.close()
    return data


def loadBinariesForPackage(package):
    variants = packages.packages[package]
    return dict([(variantId, readBinary(binaryPath(package,variant)))
                 for variantId,variant in variants.items()])

class CheckHandler(tornado.web.RequestHandler):

    def initialize(self):
        super(CheckHandler, self).initialize()

    def get(self):
        try:
            packageName = self.get_argument('package_name')
            version = self.get_argument('version', -1)
            variantId = self.get_argument('variant_id','')

            self.set_status(200)
            self.set_header('content-type','text/plain')

            packageVariants = packages.packages.get(packageName)
            if packageVariants:
                variant=packageVariants.get(variantId)
                if variant:
                    lastVersion = variant['version']
                    if lastVersion > version:
                        downloadLink = urlparse.urljoin(
                            settings.downloadHostUrl,'download/%s?package_name=%s&variant_id=%s' %
                                                     (variant['fileName'],packageName,variantId))
                        self.write('have update\n')
                        self.write(downloadLink)
                        return
            self.write('no update')
        except tornado.web.MissingArgumentError as e:
            self.set_status(400, "Param is missing: %s" % e.arg_name)

class DownloadHandler(tornado.web.RequestHandler):
    binaries = None

    def initialize(self):
        super(DownloadHandler, self).initialize()
        self.binaries = dict([(k,loadBinariesForPackage(k))
                         for k in packages.packages.keys()])

    def get(self):
        try:
            packageName = self.get_argument('package_name')
            packageBinaries = self.binaries.get(packageName)
            if packageBinaries:
                binary = packageBinaries[self.get_argument('variant_id','')]
            else:
                binary = None

            if binary:
                self.set_status(200)
                self.set_header('content-type','application/vnd.android.package-archive')
                self.write(binary)
            else:
                self.set_status(404, "Package not found")
        except tornado.web.MissingArgumentError as e:
            self.set_status(400, "Param is missing: %s" % e.arg_name)

application = tornado.web.Application([
    (r"/check", CheckHandler),
    (r"/download/.*", DownloadHandler),
    ], debug=True)

if __name__ == "__main__":
    application.listen(settings.port)
    print 'Started server on port ' , settings.port
    tornado.ioloop.IOLoop.instance().start()
