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
RUST_LOG=info
alias oura='docker run -e RUST_LOG=${RUST_LOG} -v $(pwd -W)/config/:/config -p 9186:9186 -it ghcr.io/txpipe/oura:latest'
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
make start
```

Send dummy request from a different terminal:

``` bash
# Terminal 2: send a dummy requeest for dummy purposes
make test
```

## Demo: Oura webhook

Please make sure that the Webhook Listener Server is running!

```
oura daemon --config ./config/mainnet_from_tcp_to_webhook.toml
```
## Demo: Advanced Features

### Advanced Features: Stateful Cursor

The cursor feature provides a mechanism to persist the "position" of the processing pipeline to make it resilient to restarts.

Please make sure that the Webhook Listener Server is running!

```
oura daemon --config ./config/mainnet_from_tcp_stateful_cursor.toml
```

### Advanced Features: Rollback Buffer

The "rollback buffer" feature provides a way to mitigate the impact of chain rollbacks in downstream stages of the data-processing pipeline.

```
oura daemon --config ./config/mainnet_from_tcp_rollback_buffer.toml
```

### Advanced Features: Pipeline Metrics

The metrics features allows operators to track the progress and performance of long-running Oura sessions.

```
oura daemon --config ./config/mainnet_from_tcp_pipeline_metrics.toml
```

```
curl localhost:9186/metrics
```

### Advanced Features: Mapper Options

A set of "expensive" event mapping procedures that require an explicit opt-in to be activated.

TODO

### Advanced Features: Intersect Options

Advanced options for instructing Oura from which point in the chain to start reading from.

TODO

### Advanced Features: Custom Network

Configure Oura to connect to a custom network (other than mainnet or preprod).

TODO

### Advanced Features: Retry Policy

Advanced options for instructing Oura how to deal with failed attempts in certain sinks.

TODO
