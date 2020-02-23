# Black Hole

'''
    author: grafstor
    date: 23.02.2020
'''

__version__ = 1

from tkinter import *
from random import randint
from time import sleep
from math import sqrt

class Object:
    def __init__(self, mass):
        pass

    def distance(xy1, xy2):
        return sqrt((xy2[0]-xy2[0])**2 + (xy2[1]-xy2[1])**2)

    def animate_frame(self):


class BlackHole:
    def __init__(self, mass):
        self.mass = mass

    def get_mass(self):
        return self.mass


class MainFrame:
    def __init__(self, root):
        self.root = root
        self.win_size = 900

        self.main_color = "black"
        self.alt_color = "white"
        self.mad_color = "grey50"

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

        self.stone = Object(mass=3)
        self.hole = BlackHole(mass=1000)

        self.make_field()

    def make_field(self):
        center = self.win_size//2
        listt = [i for i in range(1, 51)]
        for i in listt[::-1]:
            self.create_ball(center, center, f'grey{50 - i}', i)

    def mainloop(self):
        for i in range(1000):

            sleep(0.16)


    def create_ball(self, x, y, col="white",radius=3):
        half = radius//2
        self.canvas.create_arc(0+x-half, 0+y-half, radius+x-half, radius+y-half, 
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