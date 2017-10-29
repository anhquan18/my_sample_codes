import shutil as shl
import sys


#file_content = open(sys.argv[2],'wb')
shl.copyfile(sys.argv[1], sys.argv[2])
print 'file is copied'
#file_content.close()
