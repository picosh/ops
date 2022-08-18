#!/bin/bash

CMD=${1:-up -d}

cd prose && docker compose $CMD
cd ../lists && docker compose $CMD
cd ../pastes && docker compose $CMD
cd ../imgs && docker compose $CMD
