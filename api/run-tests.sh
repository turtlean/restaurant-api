#!/bin/bash
set -e

docker-compose run --rm -e POSTGRES_DB='dbtest' api pytest -sv
