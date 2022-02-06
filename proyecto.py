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
        if(id == 5):
           sql.pop(0) #pop que quita el name
           verifyParentesis(sql,id)
        elif(id == 6):
            if(sql[1]=='upd'):
                sql.pop(0),sql.pop(0)
                verifyParentesis(sql,id)
            else: 
                outputMessageError()
                print('el pedo fue el upd')    
         
        
    else: outputMessageError()

def verifyParentesis(sql,id):
    if '(' in sql[0] and  ')' in sql[-1]:
        nSql = "".join(sql)
        count = 0
        prueba2 = []
        
        for pos, char in enumerate(nSql):
            if(not char =='(' and not char ==')'):
                prueba2.append(char)
            else: 
                count += 1  
        c = "".join(prueba2)       
        if count > 2:
            message.config(text='[ERROR] : Cannot have multiple parentheses')
        else: 
            if(not c[-1].isalpha()):
                message.config(text ='[ERROR] : INVALID CHARACTER')
            else:
                if(id==5):
                    verifyContent(c)
                elif(id==6):
                    verifyContentFix(c)              
    else: 
        outputMessageError()


def verifyContent(data):
    tipos = ['double','bool','int','varchar'] 
    nomAndTipo = data.split(',') #CONTADOR DE COMAS
    atributos = []
    new = []
    case = True
    for elemento in nomAndTipo:
        if elemento.isalnum():
            print(elemento.isalnum(), elemento)
            atributos.append(elemento.strip())
        else: 
            case = False
            break
    #CHECAR LETA SIGUIENTE DESPUÉS DEL TIPO
    if case:    
        for t in tipos:
            for j in atributos:
                if j.find(t) > 0:
                    a = j[j.find(t)::]
                    new.append(a)      

        if len(atributos) != len(new):
            outputMessageError()
        else: message.config(text='[OK] : Struct Created Successfully')
    else: outputMessageError()

def verifyContentFix(data):
    print(data)
    new = []
    if(data[-1]== '='):
        outputMessageError()
        print('no dejar suelto un igual')
    else:
        if(data[0].isalnum()):
            fixSql = data.split('=')
            case = True
            for elemento in fixSql:
                if elemento.isalnum():
                    print(elemento.isalnum(), elemento)
                    new.append(elemento.strip())
                else: 
                    case = False
                    break
            
            if case:
                message.config(text='[OK] : Struct update Successfully')
            else: outputMessageError()    
        else: outputMessageError()
    
                    


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
