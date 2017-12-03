#!/usr/bin/env bash

mkdir -p $LOGS/supervisord
mkdir -p $LOGS/update-server

exec supervisord --nodaemon --configuration /etc/supervisord.conf
