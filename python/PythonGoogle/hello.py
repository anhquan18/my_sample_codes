##################################
#File Name: hello.py             #
#Created in 8/2017               #
##################################
###################################################################
import sys
import os
import commands as cs

###################################################################


def List(dir):
    cmd = 'ls -l ' + dir
    print 'about to do this:', cmd
    (status, output) = cs.getstatusoutput(cmd)
    
    if status:
        sys.stderr.write ('There was an error:', output)
        sys.exit(1)
    
    print output  
    filenames = os.listdir(dir)
    print filenames
    
    for filename in filenames:
        path = os.path.join(dir, filename)
        print path
        print os.path.abspath(path)  
        return


def Cat(file_name):
    try:
        f = open(file_name, 'rU')
        f_cont = f.read()
        print '----', file_name
        print f_cont
        f.close()
  
    except Exception as ec:
        print ec 


def Hello(name):
    if name == 'Alice' or name  == 'Nick':
        print 'Alert: Alice Mode'
        name = name + '???'
    else:
        print 'Else'
    
    name = name + '!!!!!'
    print 'Hello', name


def main():
    try:
        Cat(sys.argv[1])
    except IndexError as er: 
        print'Error: You forgot to input the file name'
        print er


###################################################################
if __name__ == '__main__':
  main()

