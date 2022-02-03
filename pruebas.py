import re
from tkinter import *

def cleanText(arr):
    for pos, e in enumerate(arr):
        if '(' in e:
            #insertar elemento vacio despues del  ()
            tmp = list(e)
            indice = tmp.index(('(')) + 1
            print(f'\nArray : {arr}\nelemento: {pos} caracter pos: {indice}')
            # arr.pop(pos)
            # e = ''.join(tmp)
            # arr.insert(pos, e)
            # print(arr)
            # MEJOR ELIMINAR CARACTER DEL ELEMENTO Y AGREGARLO COMO NUEVO ELEMENTO 

def verifyLex(array):
    
    # if array[0] == 'new-db':
    #     createDB(array)
    # elif array[0] == 'take':
    #     useDB(array)
    # elif array[0] == 'new-struct':  
    #     createTable(array)
    # else:
    #     print('[ERROR] : Syntax Error')
    pass

def createDB(algo):
    print(f'esto es   new-db')

def useDB(array):
    print('esto es  take')

def createTable(array):
   pass

def run():
    root = Tk()
    root.title("Entrenamiento")
    root.geometry('400x150')

    entrada = Label(root, text="Ingrese la sentencia SQL: ")
    entrada.grid(column=0,row=0)
    txt = Entry(root ,width=20)
    txt.grid(column=1,row=0)
    txt.focus()

    def getValues():
        sentencia = txt.get()
        verifyLex(cleanText(sentencia.split(' ')))

    btn = Button(root,text='Calcular',bg='red',fg='white',command=getValues)
    btn.grid(column=1,row=5)
    root.mainloop() 

run()