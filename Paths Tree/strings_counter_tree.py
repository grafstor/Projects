# Path Tree

'''
    author: graf stor
    date: 26.11.20
'''

__version__ = "1.0" 

import sys
from os import  listdir
from os.path import isfile, join, splitext
import time 

ff = open("path.txt","w",encoding='utf-8')

acceptable_extention = ['.js']

strings_sum = 0

def diir(path):
    global strings_sum

    n = []

    try:
        n = listdir(path) 
    except:
        pass

    if len(n) == 0:
        return

    for file in n:
        path_to_file = join(path, file)
        if not isfile(path_to_file):
            diir(path_to_file)

        file_extention = splitext(path_to_file)[1]


        for extention in acceptable_extention:
            if file_extention == extention:


                with open(path_to_file, 'r', encoding='utf-8') as file:
                    data = file.read()
                    if data:
                        for string in data.split('\n'):
                            if string:
                                strings_sum += 1

                ff.write(path_to_file+"\n")
                break

diir(sys.argv[1])

print('strings_sum: ', strings_sum)
