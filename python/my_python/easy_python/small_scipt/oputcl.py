import sys

#Colour 
#(\033 for escape, 1 for text style, 30-37 for the text colour, 40-47 for the background colour) 
#Put m in the end to make it worked

green =   '\033[1;32m'#45m 
black =   '\033[1;30m'#45m
red   =   '\033[1;31m'#45m
yellow =  '\033[1;33m'#45m
blue  =   '\033[1;34m'#45m
purple =  '\033[1;35m'#45m
cyan =    '\033[1;36m'#45m
white =   '\033[1;37m'#45m
l_white = '\033[0;37m'
reset =   '\033[0m'

def oput_colour():
    print 'My colourful texts'
    #print c1, 'test c1'
    print green ,'Bright Green'
    print black ,'Black'
    print red   ,'Red'
    print yellow,'Yellow'
    print blue  ,'Blue'
    print purple,'Purple'
    print cyan  ,'Cyan'
    print white ,'White', reset
    print '\n Their colourful texts'
    print("\033[0;37;40m Normal text\n")
    print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
    print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
    print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
    print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
    print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
    print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
    print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
    print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
    print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
    print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
    print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
    print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")


def main():
    oput_colour()


if __name__ == '__main__':
    main()
