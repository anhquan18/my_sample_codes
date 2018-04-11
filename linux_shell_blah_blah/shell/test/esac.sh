#!/bin/bash

case "$1" in 
    *.txt) 
        less "$1"
        ;;
    *.sh)
        vim "$1"
        ;;
    *)
        echo not supported file: $1
        ;;
esac


case "$1" in
    start|stop)
        echo "start or stop worked"
        ;;
    *)
        echo "it isn't start nor stop"
esac
