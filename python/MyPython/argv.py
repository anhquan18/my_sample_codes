##############################
# File Name: argv.py         #
# Date: 16/09/2017           #
# Author: Nguyen Anh Quan    #
##############################

###############################
import sys

###############################


print 'This is the name of the script: ', sys.argv[0]
print 'Number of argument: ', len(sys.argv)
print 'The arguments are: ', str(sys.argv)
print 'The next argument is: ', sys.argv[1], sys.argv[2]
#a = sys.argv[3]
#b = sys.argv[4]
a = sys.argv[3]
print a 
