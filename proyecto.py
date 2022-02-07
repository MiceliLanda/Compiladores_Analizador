import re
from tkinter import ttk
from tkinter import *

reservadas = [ 'new-db', 'new-struct' , 'take' , 'fix-struct', 'supr-db', 'supr-struct']
atributos = []
new = []
tokens = {
    'palabras reservadas': 0, # ASIGNADO
    'parentesisApertura' : 0,
    'parentesisCierre' : 0,
    'identificadores' : 0, #ASIGNADO
    'signo' : 0,
    'separador' : 0 ,
    'tipoDato' : 0 }

def showTokens():
    tokensCount.config(text=f'{tokens}')

def deleteValuesToken():
    for i,clave in enumerate(tokens):
        if tokens.get(clave) > 0:
            tokens[clave] = 0

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
    tokens.update({'palabras reservadas' : tokens.get('palabras reservadas')+1})
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
    tokens.update({'identificadores' : tokens.get('identificadores')+1})
    if arg.isalnum():
        if len(sql) > 0  and len(sql) < 2:
            outputMessageSuccess(id,arg)
            showTokens()
        else:
            tokensCount.config(text='') 
            outputMessageError()
    else:
        tokensCount.config(text='')
        outputMessageError()

def checkSqlAdvanced(sql, id):

    if sql[0].isalnum():
        if(id == 5):
            tokens.update({'identificadores': tokens.get('identificadores')+1})
            sql.pop(0) #pop que quita el name
            verifyParentesis(sql,id)
        elif(id == 6):
            if(sql[1]=='upd'):
                tokens.update({'identificadores': tokens.get('identificadores')+1})
                tokens.update({'palabras reservadas': tokens.get('palabras reservadas')+1})
                sql.pop(0),sql.pop(0)
                verifyParentesis(sql,id)
            else:
                message.config(text='[ERROR] : Expected reserved word UPD')
    else: 
        tokensCount.config(text='')
        outputMessageError()

def verifyParentesis(sql,id):
    if '(' in sql[0] and  ')' in sql[-1]:
        nSql = "".join(sql)
        count = 0
        prueba2 = []
        tokens.update({'parentesisApertura': tokens.get('parentesisApertura')+1})
        tokens.update({'parentesisCierre': tokens.get('parentesisCierre')+1})
        for pos, char in enumerate(nSql):
            if(not char =='(' and not char ==')'):
                prueba2.append(char)
            else:
                count += 1
        c = "".join(prueba2)
        prueba2.clear()
        if count > 2:
            message.config(text='[ERROR] : Cannot have multiple parentheses')
        else:
            if(not c[-1].isalnum()):
                message.config(text ='[ERROR] : Invalid Character')
            else:
                if(id==5):
                    verifyContent(c) # CONTAR LAS DE CONTENT COMAS
                elif(id==6):
                    separado = c.split(',')
                    if '>' in c:
                        tokens.update({'separador': tokens.get('separador')+len(separado)-1})
                        for elemento in separado:
                            if not elemento.count('>') ==1:
                                prueba2.append(elemento.replace(' ', ''))
                            else:
                                prueba2.extend(elemento.replace(' ', '').split('>'))
                                tokens.update({'palabras reservadas': tokens.get('palabras reservadas')+1})
                        # print(f' {prueba2}')
                        if '=' in prueba2[-1]:
                            verifyContentFix(prueba2)
                            prueba2.clear()
                        else:
                            prueba2.clear()
                            tokensCount.config(text='')
                            outputMessageError()

                    else:
                        if c.count('=')-1 == c.count(','):
                            co = c.split(',')
                            tokens.update({'separador': tokens.get('separador')+len(co)-1})
                            verifyContentFix(co)
                        else:
                            tokensCount.config(text='')
                            outputMessageError()
                else:
                    tokensCount.config(text='')
                    outputMessageError()


def verifyContent(data):
    tipos = ['double','bool','int','varchar']
    unknow = ''
    nomAndTipo = data.split(',') #CONTADOR DE COMAS
    tokens.update({'separador': tokens.get('separador')+len(nomAndTipo)-1})
    case = True
    for elemento in nomAndTipo:
        if elemento.isalnum():
            print(elemento.isalnum(), elemento)
            atributos.append(elemento.strip())
        else:
            case = False
            break

    if case:
        for t in tipos:
            for j in atributos:
                if j.find(t) > 0:
                    a = j[j.find(t)::]
                    if not len(a) != len(t):
                        new.append(a)
                        print(f'tipo agregado: {a}')
                    else:
                        unknow = a
        tokens.update({'tipoDato': tokens.get('tipoDato')+len(new)})
        tokens.update({'identificadores': tokens.get('identificadores')+len(new)})
        print(new)
        if len(atributos) != len(new):
            message.config(text =f'[ERROR] : Unknow Data Type {unknow}')
            new.clear()
            atributos.clear()
        else:
            message.config(text='[OK] : Struct Created Successfully')
            showTokens()
            tokensCount.config(text='')
            new.clear()
            atributos.clear()
    else:
        print('CASE ES FALSE')
        outputMessageError()

def verifyContentFix(data):
    sizeArr = len(data)
    case = True
    count = 0
    for elemento in data:
        if count != sizeArr:
            if elemento.count('=') < 2:
                count+=1
                new.append(elemento)
            else:
                case = False
                message.config(text=f'[ERROR] : Check Your Identifier')
                new.clear()
                break
    if case:
        tokens.update({'identificadores': tokens.get('identificadores')+len(new)})
        tokens.update({'signo': tokens.get('signo')+len(new)})
        for elemento in new:
            var = elemento.replace('=','')
            if var.isalnum():
                message.config(text=f'[OK] : Struct Updated Successfully')
                showTokens()
            else:
                message.config(text=f'[ERROR] : Check Your Identifier')
                tokensCount.config(text='')
                break
        new.clear()
    else:
        new.clear()
        tokensCount.config(text='')
        outputMessageError()


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
            deleteValuesToken()
            funcion(reservedWord.__getitem__(0),reservedWord)
        else:
            tokensCount.config(text='')
            message.config(text=f'[ERROR] : Syntax Error :  {reservedWord.__getitem__(0)}')

    btn = Button(root,text='Analizar',bg='green',fg='white' ,padx=70,pady=8,command=getValues)
    btn.pack(pady=30)
    global message
    global tokensCount
    message = Label(root,font=('Roboto 14 bold'), text="")
    message.pack()
    tokensCount = Label(root,font=('Roboto 14 bold'), text='')
    tokensCount.pack()
    root.mainloop()

run()
