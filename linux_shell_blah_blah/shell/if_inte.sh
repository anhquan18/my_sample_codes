#!/bin/bash

num1=$1
num2=$2

if [ $num1 -ge $num2 ]; then
    max=$num1
else 
    max=$num2
fi

echo $max
