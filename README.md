# Oura Workshop @ CARDANO BUIDLER FEST #1

## Oura repository:

The source code (Rust) of Tx-Pipe Oura is available in the following repository:
- https://github.com/txpipe/oura

Available:
- [Source code](https://txpipe.github.io/oura/installation/from_source.html)
- [Official Binary release](https://txpipe.github.io/oura/installation/binary_release.html)
- [Official Docker Image](https://txpipe.github.io/oura/installation/docker.html)
- [Guide for deploying to K8S as sidecar container](https://txpipe.github.io/oura/installation/kubernetes.html)

## Oura docker image:

Oura is available via the official docker image from Tx-Pipe:

``` bash
docker run -it ghcr.io/txpipe/oura:latest
```

## Preparation:
``` bash
# Set alias for easy access:
alias oura="docker run -v $(pwd -W)/config/:/config -it ghcr.io/txpipe/oura:latest"
# Verify:
oura --version
```

## Demo: watch

[Documentation: Oura Watch Mode](https://txpipe.github.io/oura/usage/watch.html)

``` bash
# Watch help:
oura watch --help
# Watch event stream via TCP from relay:
RELAY=relays-new.cardano-mainnet.iohk.io:3001
oura watch --bearer tcp $RELAY
```

## Demo: dump

[Documentation: Oura Dump Mode](https://txpipe.github.io/oura/usage/dump.html)

``` bash
# Demo: dump
oura dump --help
# Dump event stream via TCP from relay:
RELAY=relays-new.cardano-mainnet.iohk.io:3001
oura dump --bearer tcp $RELAY
```

## Demo: daemon

[Documentation: Oura Daemon Mode](https://txpipe.github.io/oura/usage/daemon.html)

``` bash
# Demo: daemon
oura daemon --help

# Demo: daemon with MAINNET config file
oura daemon --config ./config/mainnet_from_tcp_to_terminal.toml

# Demo: daemon with PREPROD config file
oura daemon --config ./config/preprod_from_tcp_to_terminal.toml
```

## Demo: Webhook Listener Server

Start the webhook listener server in the first terminal:

``` bash
# Terminal 1: start the server
make start-webhook-listener
```

Send dummy request from a different terminal:

``` bash
# Terminal 2: send a dummy requeest for dummy purposes
make dummy-request
```

## Demo: Oura webhook

# TODO
