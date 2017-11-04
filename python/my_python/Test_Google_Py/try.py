################################
# File Name: try.py            #
# Author: Nguyen Anh Quan      #
# Date: 30/09/2017             #
################################

import sys



def Cat(filename):
    try:
        print 'Opening the file'
        file_name = open(filename,'r')
        file_content = file_name.read()
        print file_content
    
    except Exception as er:
        print'Error with file name', er
   
 
def main():
    try:
        Cat(sys.argv[1])
  
    except IndexError as er:
        print 'Error: Trouble with Cat() function', er
  



if __name__ == '__main__':
    main()

