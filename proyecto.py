import re
from tkinter import *

tokens = {
    'palabras reservadas': 0,
    'parentesisApertura' : 0,
    'parentesisCierre' : 0,
    'identificadores' : 0,
    'signo' : 0, 
    'separador' : 0 ,
    'tipoDato' : 0
}



def createDB(algo):
    print(f'esto es   new-db')

def useDB(array):
    print('esto es  take')

def createTable(array):
   pass

def run():
    root = Tk()
    root.title("MIBA SQL Analizador")
    root.geometry('400x150')

    entrada = Label(root, text="Ingrese la sentencia SQL: ")
    entrada.grid(column=0,row=0)
    txt = Entry(root ,width=20)
    txt.grid(column=1,row=0)
    txt.focus()

    def getValues():
        sentencia = txt.get()
        # verifyLex(cleanText(sentencia.split(' ')))

    btn = Button(root,text='Analizar',bg='red',fg='white',command=getValues)
    btn.grid(column=1,row=5)
    root.mainloop() 

run()
