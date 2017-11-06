#!/usr/bin/env bash

mkdir -p $LOGS/supervisord
mkdir -p $LOGS/update-server

supervisord --nodaemon --configuration /etc/supervisord.conf
