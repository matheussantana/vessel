#!/usr/bin/env bash

_pass=$(cat ./token)
FILE="/tmp/secure.7z"
if test -f "$FILE"; then
    echo "$FILE exist"
else
    docker-compose up --build -d
    sh ./snapshot.sh
    cmd="7z a $FILE -p$_pass  -r -mhe=on ./"
    eval $cmd
fi

