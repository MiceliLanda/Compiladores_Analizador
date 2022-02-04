import re

def funcion(metodo, resto):
    resto.pop(0)
    if metodo == 'new-db':
        createDB(resto)
    elif metodo == 'take':
        takeDB(resto)
    elif metodo == 'new-struct':
        pass
    elif metodo == 'fix-struct':
        pass

def createDB(sql):
    arg = ''.join(sql)
    if arg.isalnum():
        if len(sql) > 0  and len(sql) < 2:
            print('[OK] : DB Created Successfully')
        print('[ERROR] : Check your MIBA Syntax')
    print('[ERROR] : Check your MIBA Syntax')

def takeDB(sql):
    arg = ''.join(sql)
    if arg.isalnum():
        if len(sql) > 0  and len(sql) < 2:
            print(f'[OK] : DB Used {arg}')
        print('[ERROR] : Check your MIBA Syntax')
    print('[ERROR] : Check your MIBA Syntax')

reservadas = [ 'new-db', 'new-struct' , 'take' , 'fix-struct']
entrada = input() # ENTRADA DE TEXTO
b = entrada.lower().strip().split(' ') #PARTIMOS Y QUITAMOS ESPACIOS DE LA SENTENCIA
# if b.__getitem__(0).isalpha(): #VERIFICAMOS SI CONTIENE CARACTERES ESPECIALES
if b.__getitem__(0) in reservadas: # VERIFICAMOS SI COINCIDE CON ALGUNA PALABRA RESERVADA
    funcion(b.__getitem__(0),b) # LLAMOS LA FUNCIÓN CORRESPONDIENTE
else: print(f'[ERROR] : Syntax Error :  {b.__getitem__(0)}')
# else: print(f'[ERROR] : Syntax Error :  {b.__getitem__(0)}')
