#!/bin/bash

file=$1

for file in $@
do
    if [ -d "$file" ]; then
        echo "$file is a directory:"
        ls "$file"
    elif [ -f "$file" ]; then 
        echo "$file is a regular file"
        head -n 10 "$file"
    fi
done

