#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <example>"
    exit 1
fi

cp -r .template "$1"
direnv allow "$1"
(cd "$1" && direnv exec . make init)
