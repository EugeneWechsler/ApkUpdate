
include .env

build:
	docker-compose build

up:
	docker-compose up

push:
	docker-compose -f docker-compose.yml -f docker-compose.push.yml build
	docker-compose -f docker-compose.yml -f docker-compose.push.yml push