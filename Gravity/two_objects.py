# Two gravity objects

'''
    author: graf stor
    date: 23.01.20
'''

__version__ = "2.0" 

from tkinter import *
from math import sqrt
from time import sleep
import tkinter.scrolledtext as tkscrolledtext
from random import random
import math

winS = 600

color = "black"
a_color = "red"
a2_color = "blue"

sun_size = 3
gravity_s = 150

coord_sun = (300-sun_size//2,300-sun_size//2)
coord_ball = (200,300)
xl,yl = coord_ball

ball_u_x = 0
ball_u_y = -1

sun_u_x = 0
sun_u_y = 1

iii = 0
def main_loop():
    global coord_ball, mass_ball, root,ball_u_x,ball_u_y,coord_sun,sun_u_x,sun_u_y,iii,xl,yl
    while True:
        xs, ys = coord_sun
        xb, yb = coord_ball

        # if not iii%3:
        #   canvas.create_line(xl+2,yl+2,xb+2,yb+2,fill="white")
        #   xl = xb
        #   yl = yb
        iii+=1

        r = sqrt((xs-xb)**2+(ys-yb)**2)
        # gravity_s = r*5

        sp = gravity_s / (r**2)

        min_x = xs-xb
        min_y = ys-yb

        sr_spx = sp/min_x 
        sr_spy = sp/min_y

        if xs < xb:
            ball_u_x -= sr_spx * min_x
            sun_u_x += sr_spx * min_x
        else:
            ball_u_x += sr_spx * min_x
            sun_u_x -= sr_spx * min_x

        if ys < yb:
            ball_u_y -= sr_spy * min_y
            sun_u_y += sr_spy * min_y
        else:
            ball_u_y += sr_spy * min_y
            sun_u_y -= sr_spy * min_y

        coord_ball = (xb+ball_u_x,yb+ball_u_y)
        coord_sun = (xs+sun_u_x, ys+sun_u_y)

        canvas.move(ball,ball_u_x,ball_u_y)
        canvas.move(sun,sun_u_x,sun_u_y)

        root.update()
        sleep(0.0001)

root = Tk()
root.geometry(f'{winS}x{winS}+40+40')
root.config(bg=color,
            bd=0,
            highlightthickness=0,)

canvas = Canvas(root,width=winS,height=winS)
canvas.config(bg=color,
              bd=0,
              relief='ridge',
              highlightthickness=0,)

center = winS//2 - sun_size//2

sun = canvas.create_oval(0,0,sun_size,sun_size,
                    fill=a_color,
                    outline=a_color)
canvas.move(sun,300-10,300-10)

ball = canvas.create_oval(0,0,sun_size,sun_size,
                    fill=a2_color,
                    outline=a2_color)
canvas.move(ball,coord_ball[0],coord_ball[1])

canvas.pack(side="top",fill="both")
main_loop()
mainloop()
