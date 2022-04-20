#!/bin/bash

set -e

workers=${WORKERS}
port=${PORT}

if [ "${ENV}" = "dev" ]; then
    exec gunicorn -k uvicorn.workers.UvicornWorker main:app -w "${WORKERS:=$workers}" -b :"${PORT:=$port}" --reload
fi
