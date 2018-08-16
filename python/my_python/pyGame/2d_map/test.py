from commands import getstatusoutput as gput

print "Using 'ls -a' command"
status, output = gput ('ls -a')
print status
print output
