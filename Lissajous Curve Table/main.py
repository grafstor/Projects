from tkinter import *
from time import sleep

class mainframe:
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

        self.create_field()

    def create_field(self):
        for i in range(6):
            step = i*80 + 80

            cer_x = self.canvas.create_arc(1, 1, 70, 70, 
                                      start=0,
                                      extent=359,
                                      style=ARC,
                                      outline=self.alt_color,
                                      width=1
                                      )
            self.canvas.move(cer_x, step, 0)

            cer_y = self.canvas.create_arc(1, 1, 70, 70, 
                                      start=0,
                                      extent=359,
                                      style=ARC,
                                      outline=self.alt_color,
                                      width=1
                                      )
            self.canvas.move(cer_y, 0, step)

        self.start_animation()

    def start_animation(self):
        # 9.6 second loop
        for i in range(600):
            self.animate()
            self.root.update()
            sleep(0.16)

    def animate(self):
        pass
if __name__ == "__main__":
    root = Tk()
    main = mainframe(root)
    mainloop()