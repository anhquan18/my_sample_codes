from sys import argv

try:
    a = argv[1]
except IOError:
    # Except handle the error
    print 'Error with input'
except Exception:
    print "Something isn't right"
finally:
    print 'This code will show up finally no matter what'
