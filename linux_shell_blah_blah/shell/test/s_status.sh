#!/bin/bash

ls /
echo "exit status = $?"

ls /dummy
echo "exit status = $?"

for name in aaa bbb ccc
do
    echo $name
done

for filename in *.txt file 
do
   cat $filename
done
