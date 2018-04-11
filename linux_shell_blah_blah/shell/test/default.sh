#!/bin/bash

filename=$1
file2=$2

if [ -z "$filename"  ]; then
    filename=default.txt
fi 

if [ -n "$file2"  ]; then 
    echo "it worked"
else 
    file2="nothing"
fi

echo $filename $file2
