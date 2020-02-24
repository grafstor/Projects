#Graf_AES

'''
    author: grafstor
    date: 08.01.2020
'''

__version__ = "3.0"

from pyAesCrypt import encryptFile, decryptFile
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from os.path import splitext
from os import walk, remove
from random import randint
from tkinter import *
import tkinter as tk
import time

def encrypt():
        t = time.time()

        password = main_textbox.get('1.0','end').strip()
        main_path = main_entry.get()
        
        if main_path == '':
            messagebox.showerror("Eror", "Enter path to folder")
            main_entry.focus_set()
            return

        if password[-5:] == "files":
            messagebox.showerror("Eror", "Enter password")
            main_textbox.delete('1.0', END)
            main_textbox.focus_set()
            return

        if len(password) < 512:
            ask = messagebox.askyesno(title="Ask window", message="Ganerate password?")
            if ask:
                main_textbox.delete('1.0', END)
                passw = gen_password()
                main_textbox.insert(END, passw)
                main_textbox.focus_set()
                return 

        if password == '':
            messagebox.showerror("Eror", "Enter password")
            main_textbox.focus_set()
            return


        main_textbox.delete('1.0', END)

        mypath = walk(main_path)
        lenfiles = -1

        for (dirpath, dirnames, filenames) in mypath:
            lenfiles = len(filenames)
            for file in filenames:
                path1 = "{}/{}".format(main_path,file)
                path2 = "{}/{}.aes".format(main_path,file)

                try:
                    main_textbox.insert(END,("{} encryption ...".format(file)))
                    root.update()

                    encryptFile(path1, path2, password, 65536)
                    remove(path1)

                    main_textbox.delete("end-1c linestart", "end")
                    main_textbox.insert(END,("{} encrypted\n\n".format(file)))
                    root.update()

                except:
                    main_textbox.delete("1.0", END)
                    main_textbox.insert(END,("wrong password\n\n"))
            break

        if lenfiles == -1:
            main_textbox.insert(END,("\nFolder not found\n"))
            messagebox.showinfo("INFO","Folder not found")

        elif lenfiles == 0:
            main_textbox.insert(END,("\nFolder is empty\n"))
            messagebox.showinfo("INFO","Folder is empty")

        else:
            main_textbox.insert(END,("\nRun time: {}\n".format(round(time.time() - t, 1))))
            main_textbox.insert(END,("Processed {} files".format(lenfiles)))
            messagebox.showinfo("INFO","Encryption completed")

def decrypt():
        t = time.time()

        password = main_textbox.get('1.0','end').strip()
        main_path = main_entry.get()
        
        if main_path == '':
            messagebox.showerror("Eror", "Enter path to folder")
            main_entry.focus_set()
            return

        if password[-5:] == "files":
            messagebox.showerror("Eror", "Enter password")
            main_textbox.delete('1.0', END)
            main_textbox.focus_set()
            return

        if password == '':
            messagebox.showerror("Eror", "Enter password")
            main_textbox.focus_set()
            return 

        main_textbox.delete('1.0', END)

        mypath = walk(main_path)
        lenfiles = -1

        for (dirpath, dirnames, filenames) in mypath:
            lenfiles = len(filenames)
            for file in filenames:

                path1 = "{}/{}".format(main_path,file)
                path2 = "{}/{}".format(main_path,str(splitext(file)[0]))

                try:
                    main_textbox.insert(END,("{} decryption ...\n".format(file)))
                    root.update()

                    decryptFile(path1, path2, password, 65536)
                    remove(path1)

                    main_textbox.delete("end-2c linestart", "end")
                    main_textbox.insert(END,("{} decrypted\n\n\n".format(file)))
                    root.update()

                except:
                    main_textbox.delete("1.0", END)
                    main_textbox.insert(END,("wrong password\n\n"))
            break

        if lenfiles == -1:
            main_textbox.insert(END,("\nFolder not found\n"))
            messagebox.showinfo("INFO","Folder not found")

        elif lenfiles == 0:
            main_textbox.insert(END,("\nFolder is empty\n"))
            messagebox.showinfo("INFO","Folder is empty")

        else:
            main_textbox.insert(END,("\nRun time: {}\n".format(round(time.time() - t, 1))))
            main_textbox.insert(END,("Processed {} files".format(lenfiles)))
            messagebox.showinfo("INFO","Decryption completed")

def gen_password():
    alf = list("abcdefghijklmnopqrstuvwxyz")
    k = ''
    for i in range(512):
        r = randint(0, 25)
        q = randint(1,9)
        o = randint(0,2)
        if o == 1:k += alf[r]
        elif o == 2:k += alf[r].upper()
        else:k += str(q)
    return k

def open_file():
    global main_path
    main_path = askdirectory(initialdir="C:/Users/",
                           title = "Choose a file to use.")
    main_entry.delete(0,"end")
    main_entry.insert(0, main_path)

root = tk.Tk()
root.config(bg="black")
root.iconbitmap("D:\\projects\\shifr\\3\\1.ico")
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{}x{}+{}+{}".format(500,300,screen_width//2-250, screen_height//2-150))

main_path = ''

Title = root.title( "Graf Aes")

top_frame = Frame(root)
top_frame.config(bg='grey10')

main_entry = Entry(top_frame,
           font=("Calibri",10),
           width=60,
           insertbackground="white",
           selectbackground="grey40")
main_entry.config(bd=0, bg='grey25', fg="white")
main_entry.pack(side='left', padx=5)

b3 = Button(top_frame, text="Folder")
b3.config(command=open_file,
          bd=0,
          fg="white",
          bg="grey10",
          activebackground="grey16",
          activeforeground="white",
          font="Calibri",
          padx=30,)
b3.pack(fill='x', side='left')

top_frame.pack(side='top', fill='x')

bottom_frame = Frame(root)
bottom_frame.config(bg='grey10')

main_textbox = Text(bottom_frame,height=18,width=100)
main_textbox.config(bd=0,
                    bg='grey25',
                    fg="white",
                    font=("Calibri", 8),
                    insertbackground="white",
                    selectbackground="grey40")
main_textbox.pack(side='top',padx=5)

encrypt_botton = Button(bottom_frame,
            text="Encrypt",
            width=26)
encrypt_botton.config(command=encrypt,
                      bd=0,
                      fg="white",
                      bg="grey10",
                      activebackground="grey16",
                      activeforeground="white",
                      font="Calibri",
                      pady=20,
                      padx=20,)
encrypt_botton.pack(side="left")

decrypt_botton = Button(bottom_frame,
                        text="Decrypt",
                        width=26)
decrypt_botton.config(command=decrypt,
                      bd=0,
                      fg="white",
                      bg="grey10",
                      activebackground="grey16",
                      activeforeground="white",
                      font="Calibri",
                      pady=20,
                      padx=20,)
decrypt_botton.pack(side="left")

bottom_frame.pack(side="bottom")

root.mainloop()
