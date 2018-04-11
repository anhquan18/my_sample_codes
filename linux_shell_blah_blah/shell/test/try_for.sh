#!/bin/bash

for num in $(seq 1 10)
do 
    echo $num
done

#for num in $(seq 10 100)
#do
#    touch "0${num}.txt"
#done

homesize
echo "exit status $?"
