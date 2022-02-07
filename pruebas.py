# import re

# def outputMessageError():
#     print('[ERROR] : Check your MIBA Syntax')

# def outputMessageSuccess(num, msg):
#     if num == 0:
#         print('[OK] : DB Created Successfully')
#     elif num == 1:
#         print(f'[OK] : DB Used {msg}')
#     elif num == 2:
#         print(f'[OK] : Struct {msg} DELETED')
#     elif num == 3:
#         print(f'[OK] : DB {msg} DELETED')

# def funcion(metodo, resto):
#     resto.pop(0)
#     if metodo == 'new-db':
#         createDB(resto)
#     elif metodo == 'take':
#         takeDB(resto)
#     elif metodo == 'new-struct':
#         pass
#     elif metodo == 'fix-struct':
#         pass
#     elif metodo == 'supr-struct':
#         suprStruct(resto)
#     elif metodo == 'supr-db':
#         suprDB(resto)

# def createDB(sql):
#     arg = ''.join(sql)
#     if arg.isalnum():
#         if len(sql) > 0  and len(sql) < 2:
#             outputMessageSuccess(0,arg)
#         else: outputMessageError()
#     else: outputMessageError()

# def takeDB(sql):
#     arg = ''.join(sql)
#     if arg.isalnum():
#         if len(sql) > 0  and len(sql) < 2:
#             outputMessageSuccess(1,arg)
#         else: outputMessageError()
#     else: outputMessageError()

# def suprStruct(sql):
#     arg = ''.join(sql)
#     if arg.isalnum():
#         if len(sql) > 0  and len(sql) < 2:
#             outputMessageSuccess(2,arg)
#         else: outputMessageError()
#     else: outputMessageError()

# def suprDB(sql):
#     arg = ''.join(sql)
#     if arg.isalnum():
#         if len(sql) > 0  and len(sql) < 2:
#             outputMessageSuccess(3,arg)
#         else: outputMessageError()
#     else: outputMessageError()

# reservadas = [ 'new-db', 'new-struct' , 'take' , 'fix-struct', 'supr-db', 'supr-struct']
# entrada = input() # ENTRADA DE TEXTO
# b = entrada.lower().strip().split(' ') #PARTIMOS Y QUITAMOS ESPACIOS DE LA SENTENCIA
# # if b.__getitem__(0).isalpha(): #VERIFICAMOS SI CONTIENE CARACTERES ESPECIALES
# if b.__getitem__(0) in reservadas: # VERIFICAMOS SI COINCIDE CON ALGUNA PALABRA RESERVADA
#     funcion(b.__getitem__(0),b) # LLAMOS LA FUNCIÓN CORRESPONDIENTE
# else: print(f'[ERROR] : Syntax Error :  {b.__getitem__(0)}')
# # else: print(f'[ERROR] : Syntax Error :  {b.__getitem__(0)}')


# s = 'edad2','edad=5','edad=5'
# a = len(s)
# cont = 0
# for elemento in s:
#     if cont != a:
#         if '=' in elemento:
#             cont+=1
#             print('hacer separacion por signo igual') #proceso de evaluar ->funcion
#         else: 
#             print(f'Check your variable: {elemento}')
#             break

# value = 'b=2,c=0,b=,2'

# co = value.count(',')
# ig = value.count('=')

# if value.count('=')-1 == value.count(','):
#     print('OK')
# else:
#     print('error syntax')
metodo = 'new-db'
token = {'new-db' : 1}
value = token.get(metodo)
print(value)
token.update({'new-db' : value+1})
print(token)