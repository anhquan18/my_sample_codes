import sys

print sys.argv
none,a,b,c,d = sys.argv
print a,b,c,d

if int(a) == 10 \
        and int(b) == 5 and int(c) % int(d) == 0:
        print 'Yay'
