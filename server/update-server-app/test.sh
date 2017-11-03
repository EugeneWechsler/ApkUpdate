#!/usr/bin/env bash

curl -I localhost:8888/download/org.test.package/2.02/testVariant1.apk
curl -I localhost:8888/org.test.package/testVariant1.apk
curl -d "{\"pkgname\":\org.test.package\",\"variant_id\":\testVariant1.apk\"}" -X POST localhost:8888/check