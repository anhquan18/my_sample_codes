# File Name: findall.py
# Created in 14/9/2017

#########################################
import sys
import re

#########################################

class show_the_list():
  def __init__(self,list_name):
    self.list_name = list_name

  def for_tuple(list):
    for tuple in list:
      print 


def return_tuple(tuple):
    (x, y) = tuple
    return '{0} {1}'.format(y, x)

def search_word(file_name):
   file_name = open(file_name, 'rU')
   file_content = file_name.read()
   file_name.close()
   boy_name_ranking_list = re.findall('ht.+d>(\d+)</.+d>(\w+)</t.+<t', file_content)
   girl_name_ranking_list = re.findall('ht.+d>(\d+)</.+d>(\w+)</t', file_content)
   
   for tuple in boy_name_ranking_list:
     print return_tuple(tuple)
   for tuple in girl_name_ranking_list:
     print return_tuple(tuple)
   
def main():
   search_word(sys.argv[1])
   

#########################################

if __name__ == '__main__':
   main()
