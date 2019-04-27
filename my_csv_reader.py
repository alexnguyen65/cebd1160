import os

my_file = './wine.data'

if os.path.isfile(my_file):
   print('I have a file to process')
   file = open(my_file)
   for line in file:
      my_list = line.split(',')
      print(my_list)
else:
   print('Boo, no file for me')
