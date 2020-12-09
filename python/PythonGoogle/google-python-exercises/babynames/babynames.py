#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
##############################################################
import sys
import re
import findall

##############################################################

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def returnit(tuple):
  (x,y) = tuple
  return y

def extract_names(file_name):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file_name = open(file_name, 'rU')
  file_content = file_name.read()
  file_name.close()
  boy_name_ranking_list = re.findall('ht.+d>(\d+)</.+d>(\w+)</t.+<t', file_content)
  girl_name_ranking_list = re.findall('ht.+d>(\d+)</.+d>(\w+)</t', file_content)
   
#  for tuple in boy_name_ranking_list:
#    print findall.return_tuple(tuple)
#  for tuple in girl_name_ranking_list:
#    print findall.return_tuple(tuple)  '''
  return boy_name_ranking_list, girl_name_ranking_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
#  args = sys.argv[1:]
#  if not args:
#    print 'usage: [--summaryfile] file [file ...]'
#    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
#  summary = False
#  if args[0] == '--summaryfile':
#    summary = True
#    del args[0]
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  file_name = sys.argv[1]
  (boy, girl) = extract_names(file_name) 
  boy = sorted(boy, key = returnit)
  girl = sorted(girl, key = returnit)
  file = open('baby_name_ranking_list.txt', 'w')
  
  file.write('Top 1000 famous boy names\n')
  for tuple in boy:
    file.write(findall.return_tuple(tuple)+'\n')
  file.write('\nTop 1000 famous girl names\n')
  for tuple in girl:
    file.write(findall.return_tuple(tuple)+'\n')
  file.close() 

######################################

if __name__ == '__main__':
  main()
