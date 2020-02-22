# Hilberts Curve

'''
    author: grafstor
    date: 22.02.2020
'''

from tkinter import *
from time import sleep


class MainFrame:
    def __init__(self, root):
        self.root = root
        self.win_size = 600

        self.main_color = "black"
        self.alt_color = "white"

        self.root.geometry(f'{self.win_size}x{self.win_size}+{100}+{100}')
        self.root.title("Curves")

        self.canvas = Canvas(self.root)
        self.canvas.config(bg=self.main_color,
                           height=self.win_size,
                           width=self.win_size,
                           relief='ridge',
                           highlightthickness=0,
                           )
        self.canvas.pack(fill="both")

        self.steps = 4

        self.make_field()

        li = []
        self.make_curve(li)

    def make_field(self):
        step = self.win_size // self.steps
        for i in range(1, self.steps + 1):
            self.create_line(0, step*i, self.win_size, step*i)
            self.create_line(step*i, 0, step*i, self.win_size)

    def make_curve(self, array):
        step = self.win_size // (self.steps - 1)
        change = step//2

        for i in array:
            pass

    def create_line(self, x1, y1, x2, y2):
        line = self.canvas.create_line(x1, y1, x2, y2,
                                fill=self.alt_color,
                                width=1)
        return line


if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    mainloop()
