#####################################
# File Name: check_split.py         #
# Date 08/09/2017                   #
# Author: Nguyen Anh Quan           #
#####################################


#####################################
import sys


#####################################
try:
  filename = sys.argv[1]
except:
  print 'Error'
word_list = {}

print open(filename,'rU')

file_content = open(filename,'rU')

print file_content

for line in file_content:
    print line,


