# Perimeter finding algoritm

'''
    author: grafstor
    date: 22.02.2020
'''

__version__ = "1.0"

from tkinter import *
from random import randint
from math import sin, cos, radians
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

        self.main_a = 0
        self.main_b = 0

        self.make_field()

        self.nod = self.dots_coords[self.find_top()]
        self.one(0, self.nod)

    def make_field(self):
        indent = self.win_size * 0.1
        right_bord = self.win_size - indent

        for i in range(self.dot_num):
            x, y = (randint(indent, right_bord),
                    randint(indent, right_bord))
            self.create_dot(x, y)
            self.dots_coords.append((x+3, y+3))

    def create_dot(self, x, y):
        self.canvas.create_arc(0+x, 0+y, 6+x, 6+y, 
                               start=0,
                               extent=359,
                               fill=self.alt_color,
                               outline=self.alt_color,
                               width=1,
                               )

    def one(self, angle, nod):
        tt = time.time()
        for i in range(angle, 180+angle):
            for dot in self.dots_coords:
                if dot != nod:
                    x = cos(radians(i))
                    y = sin(radians(i))
                    self.root.update()
                    if self.is_left(x, y, (dot[0] - nod[0], -(dot[1] - nod[1]))):
                        self.create_line(nod,dot)
                        if self.nod != dot:
                            self.one(i+1,dot)
                        return

    def is_left(self, x, y, xyd):
        is_is = x*xyd[1] + y*xyd[0]
        if is_is < 0:
            return False
        return True

    def find_top(self):
        x_list = []
        y_list = []

        for x, y in self.dots_coords:
            x_list.append(x)
            y_list.append(y)

        return y_list.index(min(y_list))

    def create_line(self, xy1, xy2):
        line = self.canvas.create_line(xy1[0], xy1[1], xy2[0], xy2[1],
                                       fill=self.alt_color,
                                       width=1)
        return line

if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    mainloop()
