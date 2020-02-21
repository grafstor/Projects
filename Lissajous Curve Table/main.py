#Lissajous Curves

'''
    author: grafstor
    date: 21.02.2020

'''

from tkinter import *
from time import sleep
from math import sin, radians

class LineX:
    def __init__(self, speed, begin_coords):
        self.speed = speed
        self.begin_coords = begin_coords
        self.coords = begin_coords
        self.last_cord = self.coords
        self.prom = False
        self.angle = 180

    def animate(self):
        self.angle += self.speed
        acel_x = -sin(radians(self.angle))*0.6*self.speed

        self.coords +=  acel_x
        return acel_x

    def get(self):
        return self.coords

    def get_last(self):
        self.prom = True
        return self.last_cord

class LineY:
    def __init__(self, speed, begin_coords):
        self.speed = speed
        self.begin_coords = begin_coords
        self.coords = begin_coords + 35
        self.last_cord = self.coords
        self.prom = False
        self.angle = 90

    def animate(self):
        self.angle += self.speed
        acel_x = sin(radians(self.angle))*0.6*self.speed

        self.coords +=  acel_x

        return acel_x

    def get(self):
        return self.coords

    def get_last(self):
        # self.last_cord = self.coords
        return self.last_cord

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

        self.lines_x = []
        self.lines_y = []

        self.canv_lines_x = []
        self.canv_lines_y = []

        self.steps = 6
        self.ii = 0
        self.last_cord = (0,0)

        self.create_field()

    def create_field(self):
        for i in range(self.steps):
            step = i*80 + 80

            cer_x = self.canvas.create_arc(1, 1, 70, 70, 
                                      start=0,
                                      extent=359,
                                      style=ARC,
                                      outline=self.alt_color,
                                      width=1
                                      )
            self.move_obj(cer_x, step, 0)

            cer_y = self.canvas.create_arc(1, 1, 70, 70, 
                                      start=0,
                                      extent=359,
                                      style=ARC,
                                      outline=self.alt_color,
                                      width=1
                                      )
            self.move_obj(cer_y, 0, step)

        for i in range(self.steps):
            step =  i*80 + 80

            line = LineX(i + 1, step)
            self.lines_x.append(line)

            line = self.canvas.create_line(step, 0, step, self.win_size,
                                           fill=self.alt_color,
                                           width=1)
            self.canv_lines_x.append(line)

            line = LineY(i + 1, step)
            self.lines_y.append(line)

            line = self.canvas.create_line(0, step+35, self.win_size, step+35,
                                           fill=self.alt_color,
                                           width=1)
            self.canv_lines_y.append(line)

        self.start_animation()

    def start_animation(self):

        for i in range(1000):
            self.animate()
            self.ii+=1
            self.root.update()
            # sleep(0.0)

    def move_obj(self, obj,x=0,y=0):
        self.canvas.move(obj, x, y)

    def animate(self):
        # for t in range(self.steps):

        for i in range(self.steps):
            plus = self.lines_y[i].animate()
            self.move_obj(self.canv_lines_y[i], 0, plus)
            plus = self.lines_x[i].animate()
            self.move_obj(self.canv_lines_x[i], plus, 0)
            for j in range(self.steps):
                # if not self.ii%7:
                #     line = self.canvas.create_line(cor_x, cor_y, cor_x+1, cor_y+1,
                #                                fill=self.alt_color,
                #                                width=1)
                if not self.ii%4:
                    ii = 0
                    cor_x = self.lines_x[j].get()
                    cor_y = self.lines_y[i].get()

                    lastx = self.lines_x[j].get_last()
                    lasty = self.lines_y[i].get_last()
                    # line = self.canvas.create_line(lastx, lasty, cor_x, cor_y,
                    #                        fill=self.alt_color,
                    #                        width=1)
                    line = self.canvas.create_line(cor_x, cor_y, cor_x+1, cor_y+1,
                           fill=self.alt_color,
                           width=1)
                    self.last_cord = (cor_x, cor_y)


if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    print("all")
    # mainloop()