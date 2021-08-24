#!/usr/bin/env bash

_pass=$(cat ./token)
_curpath=$(echo $PWD)
FILE="/tmp/secure.7z"

if test -f "$FILE"; then
    echo "$FILE exist"
else
    #wget -O /tmp/secure.7z https://s3.amazonaws.com/systemcall.info/fs/secure.7z
    mv secure.7z /tmp/
    cd /tmp/
    mkdir secure
    cmd="7z x secure.7z -p$_pass -o./secure/"
    eval $cmd
fi



cd /tmp/secure/
ls
docker load -i snapshot/services.img
docker images
#cd $_curpath/
sh init.sh