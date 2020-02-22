# Gift Wrapping Algorithm

'''
    author: grafstor
    date: 22.02.2020
'''

__version__ = 1

from tkinter import *
from random import randint
from math import radians, acos, asin, sqrt
from time import sleep
import time

class MainFrame:
    def __init__(self, root):
        self.root = root
        self.win_size = 600

        self.main_color = "black"
        self.alt_color = "white"

        self.root.geometry(f'{self.win_size}x{self.win_size}+{300}+{100}')
        self.root.title("Curves")

        self.canvas = Canvas(self.root)
        self.canvas.config(bg=self.main_color,
                           height=self.win_size,
                           width=self.win_size,
                           relief='ridge',
                           highlightthickness=0,
                           )
        self.canvas.pack(fill="both")

        self.dots_coords = []

        self.dot_num = 30

        self.make_field()

        self.nod = self.dots_coords[self.find_top()]
        self.one(self.nod)

    def make_field(self):
        indent = self.win_size * 0.2
        right_bord = self.win_size - indent

        for i in range(self.dot_num):
            x, y = (randint(indent, right_bord),
                    randint(indent, right_bord))
            self.create_dot(x, y)
            self.dots_coords.append((x+3, y+3))


    def one(self, nod):
        tt = time.time()
        nx,xy = nod
        array = []

        for dot in self.dots_coords:
            if dot != nod:
                x,y = dot
                x,y = (x - nx, y - xy)
                z = sqrt(x**2 + y**2)

                angele = asin(y/z)
                array.append(angele)
                self.root.update()
                
        self.create_line(nod, self.dots_coords[array.index(min(array))])

    def find_top(self):
        x_list = []
        y_list = []

        for x, y in self.dots_coords:
            x_list.append(x)
            y_list.append(y)

        return y_list.index(min(y_list))

    def create_dot(self, x, y):
        self.canvas.create_arc(0+x, 0+y, 6+x, 6+y, 
                               start=0,
                               extent=359,
                               fill=self.alt_color,
                               outline=self.alt_color,
                               width=1,
                               )

    def create_line(self, xy1, xy2):
        line = self.canvas.create_line(xy1[0], xy1[1], xy2[0], xy2[1],
                                       fill=self.alt_color,
                                       width=1)
        return line

if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    mainloop()
