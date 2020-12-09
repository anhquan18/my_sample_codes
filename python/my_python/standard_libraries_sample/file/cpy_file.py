import sys
from os.path import exists

scipt, from_file, to_file = sys.argv

print "Copying from %s  to %s"%(from_file, to_file)

# Can we close file ?
# in_data = open(from_file).read()

in_file = open(from_file, 'r') 
in_data = in_file.read()

print "The input file is %d bytes long" % sys.getsizeof(in_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit Enter to continue, Crtl - c to abort."

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print 'Alright, all done.'

out_file.close()
in_file.close()
