# Gift Wrapping Algorithm

'''
    author: grafstor
    date: 22.02.2020
'''

__version__ = 1

from tkinter import *
from random import randint
from math import radians, acos, cos, sin, sqrt, degrees
from time import sleep
# import time

class MainFrame:
    def __init__(self, root):
        self.root = root
        self.win_size = 600

        self.main_color = "black"
        self.alt_color = "white"
        self.red_color = "red"

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

        self.dot_num = 10

        self.make_field()

        nod = self.dots_coords[self.find_top()]
        self.first = nod
        self.one(nod, 0)

    def make_field(self):
        indent = self.win_size * 0.1
        right_bord = self.win_size - indent

        for i in range(self.dot_num):
            x, y = (randint(indent, right_bord),
                    randint(indent, right_bord))
            self.create_dot(x, y)
            self.dots_coords.append((x+3, y+3))



    def one(self, nod, angale):
        self.dots_coords.pop(self.dots_coords.index(nod))
        nx,ny = nod

        ax = cos(radians(angale))*30
        ay = sin(radians(angale))*30

        self.create_line(nod, (ax+nx,ay+ny))
        self.create_dot(nx-3, ny-3, self.red_color)
        array = []

        for ind in range(len(self.dots_coords)):
            x,y = self.dots_coords[ind]
            bx, by = (x - nx, -(y - ny))

            txy = ax*bx + ay*by
            sqtxy = sqrt(ax**2 + ay**2) * sqrt(bx**2 + by**2)

            angele = acos(txy/sqtxy)

            array.append(angele)

            self.root.update()
        # print(sort(array))

        print(degrees(min(array)))

        if len(self.dots_coords) == self.dot_num -1:
            self.endl = self.dots_coords[array.index(max(array))]
            self.create_dot(self.endl[0], self.endl[1], self.red_color)

        sleep(1)

        con = self.dots_coords[array.index(min(array))]

        # if con == self.endl:
        #     print(0)
        #     self.create_line(self.endl, self.first)
        # else:

        self.create_line(nod, con)
        self.one(con, degrees(min(array)))

    def find_top(self):
        x_list = []
        y_list = []

        for x, y in self.dots_coords:
            x_list.append(x)
            y_list.append(y)

        return y_list.index(min(y_list))

    def create_dot(self, x, y, col="white"):
        self.canvas.create_arc(0+x, 0+y, 6+x, 6+y, 
                               start=0,
                               extent=359,
                               fill=col,
                               outline=col,
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
