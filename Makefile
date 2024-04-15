all : build pull start stop
.PHONY : all

help:
	docker run -it ghcr.io/txpipe/oura:v1.8.5

watch:
	docker run -it entrypoint="oura watch" ghcr.io/txpipe/oura:v1.8.5