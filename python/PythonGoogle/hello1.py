#File Name: hello1.py#
#created in 7/2017   #
######################
###################################################################
import sys 

###################################################################


def Hello(name):
    '''Given a string Name and return Hello + "string Name"'''
    name = name + '!!!!!'
    print 'Hello', name


def main():
    Hello( sys.argv[1] )
   


###################################################################
if __name__ == '__main__':
  main()

