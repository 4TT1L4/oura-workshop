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
alias oura='docker rm --force oura && docker run --name oura -e RUST_LOG=${RUST_LOG} -v $(pwd -W)/config/:/config -p 9186:9186 -it ghcr.io/txpipe/oura:latest'
# Verify:d
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

Example payload:

```yaml
context:
  block_hash: e8f9c860486d6b2fe6431a2cc0d82f31d410885afdc6f278dbd0197d343892af
  block_number: 10202905
  certificate_idx: null
  input_idx: null
  output_address: null
  output_idx: null
  slot: 121885035
  timestamp: 1713451326
  tx_hash: 7d36a438a02ebf48db0387c9ac66eb6105a736f3cd562f5025c707cfa71c648f
  tx_idx: 19
fingerprint: null
metadata:
  label: '56'
  text_scalar: b4f17280c2091cc12f250402cebe1a5a74aaf85768ff,
timestamp: 1713451326000
variant: Metadata
```

For details on the data, please see the [Oura Data Dictionary](https://txpipe.github.io/oura/reference/data_dictionary.html#data-dictionary).

## Demo: Oura webhook

[Documentation: Oura Webhook Sink](https://txpipe.github.io/oura/sinks/webhook.html)

Please make sure that the Webhook Listener Server is running!

```
oura daemon --config ./config/mainnet_from_tcp_to_webhook.toml
```
## Demo: [Advanced Features](https://txpipe.github.io/oura/advanced/index.html)

[Documentation: Advanced Oura Features](https://txpipe.github.io/oura/advanced/index.html)

### Advanced Features: Stateful Cursor

[Documentation: Stateful Cursor](https://txpipe.github.io/oura/advanced/stateful_cursor.html)

The cursor feature provides a mechanism to persist the "position" of the processing pipeline to make it resilient to restarts.

Please make sure that the Webhook Listener Server is running!

```
oura daemon --config ./config/mainnet_from_tcp_stateful_cursor.toml
```

### Advanced Features: Rollback Buffer

[Documentation: Rollback Buffer](https://txpipe.github.io/oura/advanced/rollback_buffer.html)

The "rollback buffer" feature provides a way to mitigate the impact of chain rollbacks in downstream stages of the data-processing pipeline.

```
oura daemon --config ./config/mainnet_from_tcp_rollback_buffer.toml
```

### Advanced Features: Pipeline Metrics

[Documentation: Pipeline Metrics](https://txpipe.github.io/oura/advanced/pipeline_metrics.html)

The metrics features allows operators to track the progress and performance of long-running Oura sessions.

```
oura daemon --config ./config/mainnet_from_tcp_pipeline_metrics.toml
```

```
curl localhost:9186/metrics
```

### Advanced Features: Mapper Options

[Documentation: Mapper Options](https://txpipe.github.io/oura/advanced/mapper_options.html)

A set of "expensive" event mapping procedures that require an explicit opt-in to be activated:

```toml
[source.mapper]
include_block_end_events = true
include_transaction_details = true
include_transaction_end_events = true
include_block_cbor = true
include_byron_ebb = true
```

To terminal:

```
RUST_LOG=info
oura daemon --config ./config/mainnet_from_tcp_to_terminal_with_mapper_options_enabled.toml
```

To Webhook:

```
RUST_LOG=info
oura daemon --config ./config/mainnet_from_tcp_to_webhook_with_mapper_options_enabled.toml
```

### Advanced Features: Intersect Options

[Documentation: Intersect Options](https://txpipe.github.io/oura/advanced/intersect_options.html)

Advanced options for instructing Oura from which point in the chain to start reading from:
- Origin
- Tip
- Point
- Fallbacks

Advanced options for instructing Oura to stop syncing at a specific block:

```toml
[source.finalize]
until_hash = "aa83acbf5904c0edfe4d79b3689d3d00fcfc553cf360fd2229b98d464c28e9de"
```

Byron only:

```
RUST_LOG=info
oura daemon --config ./config/mainnet_from_tcp_to_webhook_byron_only.toml
```

### Advanced Features: Custom Network

[Documentation: Custom Network](https://txpipe.github.io/oura/advanced/custom_network.html)

Configure Oura to connect to a custom network (other than mainnet, preview or preprod).

For details see the [ChainConfig enum](https://github.com/txpipe/oura/blob/0e419322dba45f81f20a71f160eabbd2bfe12c3f/src/framework/mod.rs#L71-L75) in the Oura source.

```toml
[chain]
byron_epoch_length  = 432000
byron_slot_length = 20
byron_known_slot = 0
byron_known_hash = "8f8602837f7c6f8b8867dd1cbc1842cf51a27eaed2c70ef48325d00f8efb320f"
byron_known_time = 1564010416
shelley_epoch_length = 432000
shelley_slot_length = 1
shelley_known_slot = 1598400
shelley_known_hash = "02b1c561715da9e540411123a6135ee319b02f60b9a11a603d3305556c04329f"
shelley_known_time = 1595967616
address_hrp = "addr_test"
adahandle_policy = "8d18d786e92776c824607fd8e193ec535c79dc61ea2405ddf3b09fe3"
```

Further custom networks:
- https://sancho.network/
- https://cardano-community.github.io/guild-operators/#/

### Advanced Features: Retry Policy

[Documentation: Retry Policy](https://txpipe.github.io/oura/advanced/retry_policy.html)

Advanced options for instructing Oura how to deal with failed attempts in certain sinks.

```toml
[sink.retry_policy]
max_retries = 30
backoff_unit =  5000
backoff_factor = 2
max_backoff = 100000
```

TODO