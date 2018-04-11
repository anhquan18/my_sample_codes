#!/bin/bash

i=0

while [ $i -le 10 ]
do
    printf "Hello world $i\n"
    let "i += 1" 
done

let "i = 10 + 10 * 20 - 10 / 10 $1 $2"
printf "$i\n"
