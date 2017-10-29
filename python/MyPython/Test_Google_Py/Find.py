###############################
# File Name: Find.py          #
# Date 12/09/2017             #
# Author: Google              #
# Fixed by Nguyen Anh Quan    #
###############################


###############################
import re
import sys

###############################


def Find(pat, text):
  match = re.search(pat, text)
  try:
    print match.group()
  except:
    print 'Error: match not found'

def main():
  pat = input('input pat: ')
  text = input('input text: ') 
 
  Find(pat,text)



##################################
if __name__ == '__main__':
  main()  
