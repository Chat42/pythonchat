#!/usr/bin/env python
# -*- coding: utf-8 -*-

# chat - client (Tkinter)

limit = 80               # amount of lines kept inside the window
HOST = "127.0.0.1"
PORT = 5000

import sys
from string import *
from socket import *
from Tkinter import *

import thread

def listening():
    global tekst, limit
    try:
        while 1:
            temp = s.recv(1024)+chr(10)
            tekst.tag_config("a", foreground="#ffff00")
            tekst.tag_config("b", foreground="#ffffff")
            if limit % 2 == 0:
                tekst.insert(END, temp, "b")
            else:
                tekst.insert(END, temp, "a")
            tekst.see(END)
            limit -= 1
            if limit < 0:
                tekst.delete(1.0, 2.0)
    except:
        return

def say_it(event):
    global s, pole, username, limit
    inf = pole.get()
    temp = inf.encode('utf8')
    pole.delete(0, END)
    try:
        s.send(temp)
    except:
        import tkMessageBox
        tkMessageBox.showerror("Chat", "Сервер недоступен")
        sys.exit()
    return


okno = Tk()
okno.title("Chat")
photo = PhotoImage(file="fl.gif")
canv = Canvas(width=500, height=220)
item = canv.create_image(0, 0, anchor=NW, image=photo)
import tkFont
bigfont = tkFont.Font(font=("Arial", 30, "bold"))
temp = "Forgotten Lore\n (приват)"
item = canv.create_text(200, 50, text=temp, font=bigfont)
item = canv.create_text(204, 54, text=temp, font=bigfont)
item = canv.create_text(203, 53, text=temp, font=bigfont, fill="yellow")
canv.grid()
pole = Entry(okno)
pole.bind("<Return>", say_it)
pole.config(width=82, fg="black", bg="#ffaaee")
pole.grid()
import ScrolledText
tekst = ScrolledText.ScrolledText(height=12)
tekst.config(fg="black", bg="#aa66bb")
tekst.grid()

import tkSimpleDialog
HOST = tkSimpleDialog.askstring("Chat", "Введите IP:")

PORT = tkSimpleDialog.askinteger("Chat", "Введите порт:")

var = tkSimpleDialog.askstring("Chat", "Ваш ник:")
username = var.encode('utf8')

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
except:
    import tkMessageBox
    tkMessageBox.showerror("Chat", "Сервер недоступен")
    sys.exit()

try:
    strip(username)
except:
    sys.exit()
if username == "":
    sys.exit()
pole.focus()

s.send(username)
thread.start_new_thread(listening, ())

okno.mainloop()