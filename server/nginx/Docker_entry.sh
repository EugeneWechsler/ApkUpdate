#!/usr/bin/env bash

mkdir -p /var/log/nginx
dockerize -template /etc/nginx/nginx.conf.tmpl:/etc/nginx/nginx.conf

exec "$@"