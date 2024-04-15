FROM ghcr.io/txpipe/oura:v1.8.5 as oura

# Update packages and install security patches
RUN apt-get --yes update && apt-get --yes upgrade

WORKDIR /oura

COPY ./config ./

