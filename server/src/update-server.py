	# Copyright (c) 2012 Eugene Wechsler
    #
	# Licensed under the Apache License, Version 2.0 (the "License");
	# you may not use this file except in compliance with the License.
	# You may obtain a copy of the License at
    #
	# 	http://www.apache.org/licenses/LICENSE-2.0
    #
	# Unless required by applicable law or agreed to in writing, software
	# distributed under the License is distributed on an "AS IS" BASIS,
	# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	# See the License for the specific language governing permissions and
	# limitations under the License.

#!/usr/bin/python
# coding=utf-8
import urlparse
import os
import sys

from tornado import web
import tornado.ioloop
from tornado.options import define, options
import tornado.web


import packages
import settings

define("port", default=8888, help="Port to listen on", type=int)

def binaryPath(package, variant):
    return os.path.join(settings.packagesPath,package,repr(variant['version']),variant['fileName'])

class CheckHandler(tornado.web.RequestHandler):

    def initialize(self):
        super(CheckHandler, self).initialize()

    def post(self):
        try:
            print('Received check request:\n %s' % self.request.body)
            args = dict(urlparse.parse_qsl(self.request.body))
            if not args.has_key('pkgname'):

                return
            if not args.has_key('variant_id'):
                self.set_status(400, "Param is missing: variant_id")
                return

            packageName = args['pkgname']
            if not packageName:
                self.set_status(400, "Param is missing: pkgname")
            if args.has_key('version'):
                version = int(args['version'])
            else:
                version = -1

            variantId = args['variant_id']
            if not variantId:
                variantId = ''
            self.set_status(200)
            self.set_header('content-type','text/plain')

            packageVariants = packages.packages.get(packageName)
            if packageVariants:
                variant=packageVariants.get(variantId)
                if variant:
                    lastVersion = variant['version']
                    if lastVersion > version:
                        hostUrl = self.request.protocol + '://' + self.request.host
                        downloadLink = urlparse.urljoin(hostUrl,'download/%s/%s/%s' %
                                                     (packageName,variant['versionName'],variant['fileName']))
                        self.write('have update\n')
                        self.write(downloadLink)
                        return
            self.write('no update')
        finally:
            sys.stdout.flush()


def main():
    tornado.options.parse_command_line()

    application = tornado.web.Application([
        (r"/check", CheckHandler),
        (r"/download/(.*)", web.StaticFileHandler, {"path": os.path.abspath(settings.packagesPath)}),
        ], debug=True)
    application.listen(tornado.options.options.port)
    print 'Started server on port ' , options.port
    sys.stdout.flush()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()


