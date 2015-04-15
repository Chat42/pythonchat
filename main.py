#coding=utf-8
from Tkinter import *

root=Tk()
root.title('Chat42')
root.geometry('800x550')


nick = StringVar()
msg = StringVar()
quote = """Добро пожаловать в Чат 42! Здесь вы можете спокойно заниматься поиском смысла жизни, вселенной и всего остального."""



send = Button(root, text="Отправить")
change_nick = Button(root, text="Установить ник")
N_get = Label(root, text="Текущий ник: не подключен", font="Arial 18")
send_field = Entry(root, width=10, textvariable="msg", font="Arial 18")
N = Entry(root, textvariable="nick", font="Arial 18")
S = Scrollbar(root)
T = Text(root, height=4, width=70)


#def user_connect(args)
def send_msg(event):
    nick = N.get()
    msg = send_field.get()
    T.insert(END, "\n" + str(nick.encode('utf8')) + ": " + str(msg.encode('utf8')))
#def get_msg(args)
#def user_disconnect(args)
def get_nick(event):
    nick = N.get()
    N_get.configure(text = "Текущий ник: " + str(nick.encode('utf8')))
    T.insert(END, "\n" + str(nick.encode('utf8')) + "  присоединился к нам")
    send.bind("<Button-1>",send_msg)

change_nick.bind("<Button-1>",get_nick)
change_nick.pack()
N.pack()
N_get.pack()
S.pack(side=RIGHT, fill=X) #скролл-бар посмотри, что с ним сделать можно
T.pack(side=LEFT, fill=X)
S.config(command=T.xview)
T.config(yscrollcommand=S.set)
T.insert(END, quote)
send.pack() #см снизу
send_field.pack() #по-хорошему кнопку и поле ввода надо упаковать красивее, как - не придумал еще. grid-ом?
root.mainloop()