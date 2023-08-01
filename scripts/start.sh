#!/bin/sh

set -e

echo $(date '+%F %T.%3N %Z') "[flask] INFO: running start.sh"

env=${APP_ENV:-development}

if [ $env = "production" ]
then
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running production environment"
    gunicorn --bind 0.0.0.0:5000 index:app
else
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running development environment"
    export FLASK_APP=index.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    flask run --host=0.0.0.0
fi
