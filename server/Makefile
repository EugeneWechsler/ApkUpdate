
include .env

build:
	docker-compose build

up:
	docker-compose up

push:
	@docker login -u $(REGISTRY_USER) -p `cat $(REGISTRY_PASSWORD_FILE)` $(REGISTRY)
	docker-compose build
	docker tag update-server/nginx $(REGISTRY)/update-server/nginx:latest
	docker tag update-server/supervisor $(REGISTRY)/update-server/supervisor:latest
	docker push $(REGISTRY)/update-server/nginx:latest
	docker push $(REGISTRY)/update-server/supervisor:latest
	@docker logout $(REGISTRY)