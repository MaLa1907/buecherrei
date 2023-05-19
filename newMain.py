from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk

import mysql.connector
from mysql.connector import Error

py=sys.executable
# Hauptfenster erstellen
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='grey')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.title("Büchereiverwaltung")
        #self.a = StringVar()
        #self.b = StringVar()
        #self.mymenu = Menu(self)
        
        def addBook():
            os.system('%s %s' % (py,'add_book.py')) # Würde ich dir nochmal vor Ort persönlich erklären
                                                    # Kurzform: Aufrufen einer anderen Datei, 
                                                    # ohne sie im code zu importieren, sondern indem man über das dateisystem direkt darauf zugreift
        def addUser():
            os.system('%s %s' % (py,'add_user.py'))    
        
        # Button erstellen
        self.button = Button(self, text='Buch hinzufügen', width=25, font=('Arial', 10), command=addBook).place(x=240,y=250)
        self.button = Button(self, text='Benutzer hinzufügen', width=25, font=('Arial', 10), command=addUser).place(x=540,y=250)
        
        # Tabelle erstellen
        self.listTree = ttk.Treeview(self,height=14,columns=('Kunde','Buch','Ausgeliehen am','Rückgabe am'))
        #self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        #self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=50,minwidth=50,anchor='center')
        self.listTree.heading("Kunde", text='Kunde')
        self.listTree.column("Kunde", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Buch", text='Buch')
        self.listTree.column("Buch", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Ausgeliehen am", text='Ausgeliehen am')
        self.listTree.column("Ausgeliehen am", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Rückgabe am", text='Rückgabe am')
        self.listTree.column("Rückgabe am", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=320,y=360)
        #self.vsb.place(x=1028,y=361,height=287)
        self.hsb.place(x=320,y=650,width=700)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))
        
MainWin().mainloop()