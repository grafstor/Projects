# White tree

'''
    author: grafstor
    date: 27.04.2020
'''

__version__ = "1.0"

from random import randint
from time import sleep
from graphics import *
from math import sin, cos, radians

winS = 700

win = GraphWin("Tree", winS, winS) 
win.setBackground("black")

def main(a):
    stack = [a]
    tmp = a['i']
    while len(stack) != 0:
        item = stack.pop(0)
        if item['i']<=0:
            continue
        # if item['i']<tmp:
        #     tmp = item['i']
        #     sleep(0.2)

        xx = round(cos(radians(item['r'])) * item['b']) + item['x']
        yy = round(sin(radians(item['r'])) * item['b']) + item['y']

        s = Line(Point(item['x'], item['y']), Point(xx, yy))
        s.draw(win)
        s.setWidth(item['i']//1.5)
        s.setFill("white")

        i = randint(-30,30)
        stack.append({'i': item['i']-1,'b': item['b'], 'r':item['r']+i, 'x':xx, 'y':yy})

        if i%2==0:
            stack.append({'i': item['i']-1,'b': item['b'], 'r':item['r']-i, 'x':xx, 'y':yy})

first = {'i': 18,'b': 20, 'r':270, 'x':winS//2, 'y':winS-30}
main(first)


print("Done!")

win.getMouse()
win.close()









