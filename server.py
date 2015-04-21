#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# chat
# server
 
import sys
from string import *
from socket import *
import thread
 
HOST = ""
PORT = 5000
 
try:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)
except:
    raw_input("Can't setup server!\n")
    sys.exit()
 
print "Server is ready!"
print "Listening at: ", s.getsockname()
 
def listening(conn, addr, username):
    global clients
    while 1:
        try:
            temp = conn.recv(1024)
        except:
            return
        dane = username + ": " + temp
        for i in range(0, (len(clients)/3)):
            try:
                clients[i*3].send(dane)
            except:
                pass
    return
 
def manager():
    global s, clients
    while 1:
        conn, addr = s.accept()
        username = strip(conn.recv(1024))
        thread.start_new_thread(listening, (conn, addr, username))
        old = 0
        for i in range(0, len(clients)/3):
            if clients[i*3] == conn:
                old = 1
                break
        if old == 0:
            clients.append(conn)
            clients.append(addr)
            clients.append(username)
    return
 
clients = []
thread.start_new_thread(manager, ())
while 1:
    menu = "\nCommands:\n\n"
    menu += "! - shut down\n"
    menu += "? - status\n"
    menu += "\n>"
    result = raw_input(menu)
    if strip(result) == "!":
        s.close()
        sys.exit()
    if strip(result) == "?":
        for i in range(0, (len(clients)/3)):
            try:
                print clients[i*3+2], "at: ", clients[i*3].getpeername()
            except:
                pass
