import sys

def Try(argument):
   print argument

def main():
    try:
        Try(sys.argv[1])
    except Exception as ex:
        print 'try worked'
        print ex
if __name__ == '__main__':
    main()
