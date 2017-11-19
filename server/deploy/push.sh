#!/usr/bin/env bash

export MYDIR=$(dirname "${BASH_SOURCE[0]}")
eval $(docker-machine env $DOCKER_MACHINE)
docker-compose -f $MYDIR/../docker-compose.yml -f $MYDIR/../docker-compose.push.yml build
docker-compose -f $MYDIR/../docker-compose.yml -f $MYDIR/../docker-compose.push.yml push
