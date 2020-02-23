# Console

'''
    author: graf stor
    date: 02.01.20
'''

__version__ = "2.0" 

import tkinter as tk
import tkinter.scrolledtext as tkscrolledtext
from tkinter import *
from os import startfile, listdir, remove, rename, mkdir

class terminal:
    def __init__(self, name="Console", theme="black"):

        if theme == "black":
            a_theme = "white"

        else:
            a_theme = "black"

        self.root = tk.Tk()
        self.root.title( name )
        # self.root.iconbitmap('1.ico') # если есть иконка

        self.border = 2.0

        self.check = False

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        window_width = self.screen_width/1.7
        window_height = self.screen_width/3
        window_position_x = self.screen_width/2 - window_width/2
        window_position_y = self.screen_height/2 - window_height/2
        self.root.geometry('%dx%d+%d+%d' % (window_width, window_height, window_position_x, window_position_y))

        frame = tk.Frame(self.root, bg=theme)
        frame.pack(side="bottom", fill='both', expand='no')

        self.textbox = tkscrolledtext.Text(master=frame,
                                            wrap='word',
                                            width=int(window_width),
                                            height=int(window_height)) #width=characters, height=lines
        self.textbox.pack(side='top',
                            fill='y',
                            expand=True,
                            padx=0,
                            pady=0)
        self.textbox.config(bg = theme,
                            fg=a_theme,
                            selectbackground=a_theme,
                            yscrollcommand=1,
                            highlightbackground=theme,
                            insertbackground=a_theme,
                            font="Courier",
                            foreground=a_theme,
                            padx=1,
                            )
        self.textbox.bind('<Return>', self.get_text)
        self.textbox.focus_set()
        self.insert_text("You in Graf Console\nWrite help to find out commands")


    def get_text(self, must):
        ''' text from main textbox'''
        text = self.textbox.get(str(self.border), 'end').strip()
        self.border += 1
        if text != '':
            print("LOG INFO: NEW.TEXT INPUT := '{}'".format(text.strip()))
            self.check = True
            # сканирование главного текста 
            self.scan(text) # потом

    def insert_text(self, text=''):
        ''' text to main textbox'''
        if self.check:
            text = "\n" + text
        else:
            text = text + "\n"
        self.textbox.insert('end', text)
        self.border += 1
        self.check = False

    def scan(self, text):
        # убираю переносы
        text = text.strip()
        # разбиваю на список
        n_text = text.split()
        n_text = [i.lower() for i in n_text]
        # команды 
        if text != '':
            # закрытие программы
            if text.lower() == "exit":
                self.root.quit()
            # отчистка поля
            elif text.lower() == "cls":
                self.textbox.delete("1.0", 'end')
                self.border = 2.0

    def start(self):
        '''start main loop'''
        self.root.mainloop()

# self.textbox.config(state=DISABLED)

Graf = terminal("GConsole")

Graf.start()