#!/usr/bin/env bash

echo localhost:8888/download/org.test.package/2.02/testVariant1.apk
curl -isb -X GET localhost:8888/download/org.test.package/2.02/testVariant1.apk

echo localhost:8888/org.test.package/testVariant1.apk
curl -isb -X GET localhost:8888/org.test.package/testVariant1.apk

echo POST localhost:8888/check
curl -isb -X POST -d "pkgname=org.test.package&variant_id=variant1&version=1" localhost:8888/check