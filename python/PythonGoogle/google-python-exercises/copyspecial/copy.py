#####################################
# File Name: copy.py                #
# Date: 18/09/2017                  #
# Author: Nguyen Anh Quan           #
#####################################

######################################
import shutil as shl
import os
from commands import getstatusoutput as gtst

######################################


def copyall(dir):
  if dir:
    print 'The dir has already existed'
  else:
    cmd = 'pwd'
    print 'About to use pwd command'
    (status, output) = gtst(cmd)
    os.mkdir(output+'/'+str(dir),0777)
    copy
