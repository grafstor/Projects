# Delete Tree
# WARNING!:REMOVE A LOT FROM DISK C

'''
    author: graf stor
    date: 11.01.20
'''

__version__ = "1.0" 

from os import listdir, remove
from os.path import isfile

def diir(a,f,t):

    n = []

    try:
        n = listdir(f +"\\"+ t) 
    except:
        pass

    if len(n) == 0 or a == 0:
        return

    for i in n:
        if not isfile(f +"\\"+ t + "\\" + i):
            try:
                diir(a-1,f +"\\"+t, i)
            except:
                pass

        else:
            try:
                remove(f +"\\"+ t + "\\" + i)
            except:
                pass

# diir(4,"C:","")
