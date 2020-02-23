# NotePad

'''
    author: graf stor
    date: 09.01.20
'''

__version__ = "1.0" 

from tkinter import *
from tkinter import filedialog as fd
import codecs
import sys


class MainNote:
    def __init__(self,root,ppath=''):
        self.root = root
        self.mainmenu = Menu(self.root) 
        self.root.config(menu=self.mainmenu,
                         bg="black")

        theme = "grey10"
        b_theme = "grey15"
        a_theme = "white"
        sel_theme = "grey30"

        self.file_name = ppath
         
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Открыть...",command=self.open)
        self.filemenu.add_command(label="Новый",command=self.new)
        self.filemenu.add_command(label="Сохранить...",command=self.save)
        self.filemenu.add_command(label="Выход", command=self.quit)

        self.filemenu.config(bg=theme,
                             fg=a_theme,
                             activebackground=sel_theme,
                             activeborderwidth=4,
                             tearoff=0)
         
        self.mainmenu.add_cascade(label="Файл", menu = self.filemenu)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        window_width = self.screen_width/1.7
        window_height = self.screen_width/3
        window_position_x = self.screen_width/2 - window_width/2
        window_position_y = self.screen_height/2 - window_height/2
        self.root.geometry('%dx%d+%d+%d' % (window_width, window_height, window_position_x, window_position_y))

        frame = Frame(self.root, bg=theme)
        frame.pack(side="bottom", fill='both', expand='no')

        self.textbox = Text(master=frame,
                            wrap='word',
                            width=int(window_width),
                            height=int(window_height)) #width=characters, height=lines

        scroll = Scrollbar(frame,command=self.textbox.yview)
        scroll.config(activebackground=theme,
                      bd=0,
                      highlightbackground=theme,
                      elementborderwidth=0)
        scroll.pack(side=RIGHT, fill=Y)

        self.textbox.pack(side='top',
                            fill='y',
                            expand=True,
                            padx=0,
                            pady=0)
        self.textbox.config(bg = theme,
                            fg=a_theme,
                            selectbackground=sel_theme,
                            highlightbackground=theme,
                            insertbackground=a_theme,
                            font=("Candara",10),
                            foreground=a_theme,
                            padx=1,
                            yscrollcommand=scroll.set,
                            )
        self.textbox.focus_set()
        
        if self.file_name != '':
            self.open()

    def quit(self):
        self.root.quit()

    def save(self):
        if self.file_name == '':
            self.file_name = fd.asksaveasfilename(filetypes=(("All files", "*.*"),
                                                        ("TXT files", "*.txt")),
                                                title = "Path to save")

        file = codecs.open(self.file_name,"w",encoding='utf-8')
        text = self.textbox.get('1.0','end')
        file.write(text)
        file.close()

    def open(self):
        if self.file_name == '':
            self.file_name = fd.askopenfilename(filetypes=(("All files", "*.*"),
                                                        ("TXT files", "*.txt")),
                                                title = "Path to open")

        if self.file_name == '':
            self.open()

        file = codecs.open(self.file_name,"r", "utf_8_sig")
        self.textbox.delete('1.0', END)
        self.textbox.insert(END,file.read())
        file.close()

    def new(self):
        self.file_name = ''
        self.textbox.delete('1.0', END)

if __name__ == "__main__":
    path = ''

    if len (sys.argv) > 1:
        path = sys.argv[1]

    root = Tk()
    root.title("Graf NotePad")
    root.iconbitmap("1.ico")
    graf = MainNote(root,path)
    root.mainloop() 