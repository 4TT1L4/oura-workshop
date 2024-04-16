all : build pull start stop
.PHONY : all

help:
	docker run -it ghcr.io/txpipe/oura:v1.8.5

watch:
	docker run -it entrypoint="oura watch" ghcr.io/txpipe/oura:v1.8.5

start-webhook-listener:
	docker compose down
	docker compose up -d --build --remove-orphans webhook-listener
	docker compose logs -f

dummy-request:
	curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:8095/webhook