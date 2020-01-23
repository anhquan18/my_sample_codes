import sys

# put * before your vari -> it will turn into (a, b, c) when it receive a, b, c parameter
def one_para(*argv):
    return argv

def one_list(a_list):
    return a_list

def main():
    a = one_para(1, 2, 'Hi', 'Hello')
    b = one_list (sys.argv)
    print a, b

if __name__ == '__main__':
    main() 
