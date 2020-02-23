# Pi number count

'''
    author: grafstor
    date: 23.02.2020
'''

__version__ = 1

from tkinter import *
from random import randint
from time import sleep
from math import sqrt

class MainFrame:
    def __init__(self, root):
        self.root = root
        self.win_size = 900

        self.main_color = "black"
        self.alt_color = "white"

        self.root.geometry(f'{self.win_size}x{self.win_size}+{300}+{100}')
        self.root.title("PI")

        self.canvas = Canvas(self.root)
        self.canvas.config(bg=self.main_color,
                           height=self.win_size,
                           width=self.win_size,
                           relief='ridge',
                           highlightthickness=0,
                           )
        self.canvas.pack(fill="both")

        self.make_field()
        self.mainloop()

    def make_field(self):
        self.canvas.create_arc(0, 0, self.win_size - 1, self.win_size - 1,
                               outline=self.alt_color,
                               extent=359.999,
                               style="arc",
                               width=1,
                               )

    def mainloop(self):
        num_in = 0 
        half = self.win_size//2
        for i in range(1,100000000):
            x, y = (randint(-half, half),
                    randint(-half, half))
            rad = sqrt(x**2 + y**2)

            if rad < half:
                num_in += 1
                self.create_dot((x+half,y+half))
            else:
                self.create_dot((x+half,y+half),"red")

            if not i % 1000:
                self.root.update()
                print((num_in/i)*4)

    def create_dot(self, xy, color='white', radius=1):
        half = radius//2
        dot = self.canvas.create_arc(0, 0, radius, radius, 
                               extent=359.999,
                               fill=color,
                               outline=color,
                               width=1,
                               )
        self.canvas.move(dot, xy[0]-half, xy[1]-half)

if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    mainloop()