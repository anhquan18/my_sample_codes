#############################
# File Name: check.py       #
# Date: 16/09/2017          #
# Author: Nguyen Anh Quan   #
#############################

#######################################
import os, sys, commands as cs, re

#######################################


def show_path(dir):
  all_file = [] 
  print os.listdir(dir)
  for file in os.listdir(dir):
    match = re.search(r'.+__\w+__.+', file)
    if match:
      print match.group()
      all_file.append(match.group())
      print os.path.abspath(os.path.join(dir, match.group()))

#def copy_file(dir):
    

def main():
  show_path(sys.argv[1])

####################################################

if __name__ == '__main__':
  main()
