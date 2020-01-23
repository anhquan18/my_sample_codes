import time

def check_print():
    start = time.time()
    for i in range(10000):
        print 'This will show how long does it take to print'
    print '\tTime: {} seconds'.format(time.time() - start)

check_print()
