# pico-ops

This repository contains ops utils (such as our monitoring system)
as well as scripts that we use on a day-to-day basis.

- `monitoring` defines the monitoring system we use for pico servers.
  The monitoring system is composed of two main services: grafana and prometheus.

- `scripts` defines the scripts we use at pico.

# triage

## HTTPS or SSH is inaccessible

Run `/opt/oracle/setup_network.sh` in the VM where the service lives
