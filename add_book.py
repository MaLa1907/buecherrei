from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

# Fenster erstellen
class AddBookWindow(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Buch hinzufügen')
        self.canvas = Canvas(width=500, height=500, bg='gray')
        self.canvas.pack()
        #a = StringVar() # Stringvars nehmen die Daten in den TExtfeldern entgegen, und packen Sie in eine Variable mit der wir weiterarbeiten können
        booknameInput = StringVar()
        authornameInput = StringVar()
        
        # Eingaben überprüfen
        def addBook():
            if len(booknameInput.get()) == 0 or len(authornameInput.get()) == 0: # Ist eines der Eingabefelder leer?
                messagebox.showerror("Fehler","Bitte geben Sie einen Buchnamen/Autor an!")
            else:
                g = 'TRUE' # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
                try:
                    self.conn = mysql.connector.connect(host='localhost', # Verbindung mit der Datenbank aufbauen
                                         database='library_management',
                                         user='root',
                                         password='3956')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into books(name,author,availability) values (%s,%s,%s)",[booknameInput.get(),authornameInput.get(),g])
                    self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben
                    messagebox.showinfo('Erfolg', "{} wurde hinzugefügt!".format(booknameInput.get())) #Infofenster bei Erfolg
                    ask = messagebox.askyesno("Info", "Möchten Sie ein weiteres Buch hinzufügen") # Noch ein Buch hinzufügen?
                    if ask:             # Wenn Ja: 
                        self.destroy()  # Aktuelles fenster schliesen
                        os.system('%s %s' % (py, 'add_Book.py'))    # Und add_book wieder neu öffnen
                    else:
                        self.destroy() # Wenn Nein: "Buch hinzufügen" Fenster schließen
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message
        
        # Labels und Textfelder erstellen
        Label(self, text='').pack()
        Label(self, text='Buch hinzufügen:',bg='gray',fg='black',font=('Arial', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Buchname:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=booknameInput, width=30).place(x=170, y=182)
        Label(self, text='Autor:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=authornameInput, width=30).place(x=170, y=232)
        Button(self, text="Hinzufügen", command=addBook).place(x=245, y=300)
AddBookWindow().mainloop()