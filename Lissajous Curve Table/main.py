from tkinter import *
from time import sleep
from math import sin, radians

class Line:
    def __init__(self, speed, begin_coords):
        self.speed = speed
        self.begin_coords = begin_coords
        self.coords = begin_coords
        self.direct = True

    def animate(self):
        acel_x = 70
        now = self.coords - self.begin_coords

        if now >= 70:
            self.direct = False
            now = 70

        elif now <= 0:
            self.direct = True
            now = 1
        #вычислени
        if self.direct:
            acel_x = sin(radians(now * self.speed))
        else:
            acel_x = -sin(radians(now * self.speed))

        self.coords +=  acel_x
        return acel_x

    def get_x(self):
        return self.coords

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

        self.lines = []

        self.canv_lines_x = []
        self.canv_lines_y = []

        self.create_field()

    def create_field(self):
        for i in range(3):
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

        for i in range(3):
            step =  i*80 + 80
            line = Line(i + 1, step)
            self.lines.append(line)

            line = self.canvas.create_line(step, 0, step, self.win_size,
                                           fill=self.alt_color,
                                           width=1)
            self.canv_lines_x.append(line)

            line = self.canvas.create_line(0, step, self.win_size, step,
                                           fill=self.alt_color,
                                           width=1)
            self.canv_lines_y.append(line)

        self.start_animation()

    def start_animation(self):
        # 9.6 second loop
        for i in range(1000):
            self.animate()
            self.root.update()
            sleep(0.016)

    def move_obj(self, obj,x=0,y=0):
        self.canvas.move(obj, x, y)

    def animate(self):
        for i in range(3):
            plus = self.lines[i].animate()
            self.move_obj(self.canv_lines_x[i], plus, 0)
            self.move_obj(self.canv_lines_y[i], 0, plus)

if __name__ == "__main__":
    root = Tk()
    main = MainFrame(root)
    print("all")
    mainloop()