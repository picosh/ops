#!/bin/bash

FILTER=${1:-prose|lists|pastes}

function _exit {
	kill $(jobs -p)
}

trap _exit EXIT

for name in $(docker ps --format "{{.Names}}" | egrep "$FILTER"); do
	eval "docker logs -f --tail=5 \"$name\" 2>&1 | sed -e \"s/^/[-- $name --] /\" &";
done

wait
