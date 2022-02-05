import re
from tkinter import ttk
from tkinter import *

reservadas = [ 'new-db', 'new-struct' , 'take' , 'fix-struct', 'supr-db', 'supr-struct']

tokens = {
    'palabras reservadas': 0,
    'parentesisApertura' : 0,
    'parentesisCierre' : 0,
    'identificadores' : 0,
    'signo' : 0, 
    'separador' : 0 ,
    'tipoDato' : 0 }

def outputMessageError():
    message.config(text='[ERROR] : Check your MIBA Syntax')

def outputMessageSuccess(num, msg):
    if num == 0:
        message.config(text='[OK] : DB Created Successfully')
    elif num == 1:
       message.config(text=f'[OK] : DB Used {msg}')
    elif num == 2:
        message.config(text=f'[OK] : Struct {msg} Deleted')
    elif num == 3:
        message.config(text=f'[OK] : DB {msg} Deleted')

def funcion(metodo, resto):
    # AQUI INICIAREMOS EL CONTEO DE RESERVADAS
    resto.pop(0)
    if metodo == 'new-db':
        checkSql(resto,0)
    elif metodo == 'take':
        checkSql(resto,1)
    elif metodo == 'new-struct':
        checkSqlAdvanced(resto,5)
    elif metodo == 'fix-struct':
        checkSqlAdvanced(resto,6)
    elif metodo == 'supr-struct':
        checkSql(resto,2)
    elif metodo == 'supr-db':
        checkSql(resto,3)

def checkSql(sql, id):
    arg = ''.join(sql)
    if arg.isalnum():
        if len(sql) > 0  and len(sql) < 2:
            outputMessageSuccess(id,arg)
        else: outputMessageError()
    else: outputMessageError()

def checkSqlAdvanced(sql, id):
    if sql[0].isalnum():
        sql.pop(0)
        verifyParentesis(sql)
    else: outputMessageError()

def verifyParentesis(sql):
    if '(' in sql[0] and  ')' in sql[-1]:

        nSql = "".join(sql)
        print(nSql)
        prueba = []
        count = 0
        prueba2 = []
        
        for pos, char in enumerate(nSql):
            if(not char =='(' and not char ==')'):
                
                prueba2.append(char)
                
            if(str(char).isalnum()):
                prueba.append(char)
            else:
                if(char == '(' or char == ')'): 
                    count += 1  

        b = "".join(prueba) 
        c = "".join(prueba2)       
        print(b)
        print('Esto es c',c)
        #print(nSql)
        #nSql.pop(0), nSql.pop(-1)
        if count > 2:
            message.config(text='[ERROR] : Cannot have multiple parentheses')
        else: 
            if(not c[-1].isalpha()):
                message.config(text ='[ERROR] : INVALID CHARACTER')
            else:  
                verifyContent(c) 
            
            #CHECAR LO QUE TIENE DENTRO DE LOS PARENTESIS -> NUEVA FUNCION
    else: 
        outputMessageError()


def verifyContent(data):

    tipos = ['varchar','bool','int','double'] # i
    nomAndTipo = data.split(',') #CONTADOR DE COMAS
    atributos = []
    for elemento in nomAndTipo:
        if elemento.isalnum():
            atributos.append(elemento.strip())

    if atributos:
        for t in tipos:
            for j in atributos:
                if j.find(t) > 0:
                    message.config(text ='[OK] : Struct Created Successfully')
                else: 
                    outputMessageError()
                    break


def run():
    root = Tk()
    root.title("MIBA SQL Analizador")
    root.geometry('600x350')

    lbl = Label(root,text="Ingresa la sentencia de MIBA",font=('Roboto 16 ') )
    lbl.pack()
    text=Entry(root, font = ('Roboto 15'),width=50)
    text.insert(END, "")
    text.pack(pady=30)

    def getValues():
        sentencia = text.get()
        reservedWord = sentencia.lower().strip().split(' ')
        if reservedWord.__getitem__(0) in reservadas: 
            funcion(reservedWord.__getitem__(0),reservedWord) 
        else: 
            message.config(text=f'[ERROR] : Syntax Error :  {reservedWord.__getitem__(0)}')

    btn = Button(root,text='Analizar',bg='green',fg='white' ,padx=70,pady=8,command=getValues)
    btn.pack(pady=30)
    global message
    message = Label(root,font=('Roboto 14 bold'), text="")
    message.pack()
    root.mainloop() 

run()
