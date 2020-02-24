# White tree

'''
    author: grafstor
    date: 03.12.2019
'''

__version__ = "1.0"

from random import randint
from time import sleep
from graphics import *
from math import sin, cos, radians

winS = 700

win = GraphWin("Tree", winS, winS) 
win.setBackground("black")

def tree(i,a,b=60,r=270,x=winS//2,y=winS-30):

    if a <= 0 or b < 2: 
        return

    xx = round(cos(radians(r)) * b) + x
    yy = round(sin(radians(r)) * b) + y

    s = Line(Point(x, y), Point(xx, yy))
    s.draw(win)
    s.setWidth(a//1.5)
    s.setFill("white")

    i = randint(-30,30)
    tree(i, a-1, b , r + i, xx, yy)

    if i%2==0:
        tree(i, a-1, b , r - i, xx, yy)

tree(10,20,16,270)

print("Done!")

win.getMouse()
win.close()

