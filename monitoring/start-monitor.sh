#!/bin/bash

docker run -d --name node_exporter \
    --net host \
    --pid host \
    --restart always \
    -v /:/host:ro,rslave \
    quay.io/prometheus/node-exporter --path.rootfs=/host

docker run -d --name cadvisor \
    --restart always \
    -v /:/rootfs:ro \
    -v /var/run:/var/run:ro \
    -v /sys:/sys:ro \
    -v /var/lib/docker/:/var/lib/docker:ro \
    -v /dev/disk/:/dev/disk:ro \
    --device /dev/kmsg:/dev/kmsg \
    --privileged \
    -p 9080:8080 \
    gcr.io/cadvisor/cadvisor:v0.44.1-test
