#!/bin/bash

if [ $1 -ne 10 ] && [ $2 -ne 1 ]; then 
    exit 10
fi

echo "never reach here if $1 and $2 are numbers"
ls "$1"
