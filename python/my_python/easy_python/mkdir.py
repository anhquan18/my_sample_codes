#!/usr/bin/python

import os, sys

# Path to be created
#You can input only dir or the dir path any way will work fine with os.mkdir
dir  = "Me"
path = '/home/nguyen/python/MyPython/Me'
os.mkdir(path, 0777)
print "Path is created"
