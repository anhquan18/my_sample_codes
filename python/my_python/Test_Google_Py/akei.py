#############################
# File Name: akei.py        #
# Date: 09/09/2017          #
# Author: Nguyen Anh Quan   #
#############################


#############################################
import sys

#############################################


def rank_list(tuple):
    x, y = tuple
    return y


def word_count(file_name):
    word_list = {}
    try:
        file_name = open(file_name,'rU')
        file_content = file_name.read()
        file_name.close()
    except Exception as er:
        print 'Error: problem with', file_name, er
       
    for word in file_content.split():
        if word in word_list:
            word_list[word] += 1
        else:
   	        word_list[word] = 1
   
    ranking_list = sorted(word_list.items(), key = rank_list, reverse = True)
    top_ten = []
    i = 0
   
    print 'This is the top ten ranking list'
    for tuple in ranking_list:
        top_ten.append(tuple)
        print top_ten[i]
        i += 1
        if i == 10:
            break
  
    print '\nThis is the word list: '
    for tuple in word_list.items():
        print tuple


def main():
    try:
        word_count(sys.argv[1])
    except IndexError as er:
        print 'IndexError: problem with word_count parameter', er


###################################################
if __name__ == '__main__':
  main()


