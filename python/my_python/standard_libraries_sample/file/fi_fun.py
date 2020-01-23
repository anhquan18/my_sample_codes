def main():
    f = open('Data.txt', 'r')
    
    # get whole file as big str
    f.read()
    # return a line after you called and return the next line ('\n') in the next time you call
    f.readline()
    # return a list of lines of whole file
    f.readlines()
    # bring the read head use in readline() to the line number n of file
    n = 0
    f.seek(n)
