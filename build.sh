#!/bin/sh

#wait for postgres up 
./docker/flask/wait-for-it.sh ${DB_HOSTNAME}:${DB_PORT} --timeout=100
status_postgres=$?


if [ $status_postgres -gt 0 ]; then
    echo "postgres is not ready"
    exit $status
fi

make clean
make upgrade
make init
make run-prod