# Path Tree
# Write all file from disk C

'''
    author: graf stor
    date: 11.01.20
'''

__version__ = "1.0" 

from os import startfile, listdir
from os.path import isfile
import time 

ff = open("path.txt","w",encoding='utf-8')

def diir(a,f,t):

    n = []

    try:
        n = listdir(f +"\\"+ t) 
    except:
        pass

    if len(n) == 0:
        return

    for i in n:
        if not isfile(f +"\\"+ t + "\\" + i):
            diir(a-1,f +"\\"+t, i)

        else:
            ff.write(f +"\\"+ t + "\\" + i+"\n")

# diir(3,"C:","")
