iport os

black =   '\033[1;30m'
red   =   '\033[1;31m'
green =   '\033[1;32m' 
yellow =  '\033[1;33m'
blue  =   '\033[1;34m'
magneta=  '\033[1;35m'
cyan =    '\033[1;36m'
white =   '\033[1;37m'
reset =   '\033[0;37m'
esc =     '\033[0m'

if os.isatty(1):
    flag = True

def output_color(use_color, num):
    if use_color:
        print red+str(num)+esc
        print 'next'
    else:
        print str(num)

for num in range(1000):
    output_color(flag, num)
