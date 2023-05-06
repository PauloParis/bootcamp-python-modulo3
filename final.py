
# modificar lista de magos
def hacer_grandioso(magos):
    return list(map(lambda x: 'El gran ' + x, magos))

# imprimir la lista original
def imprimir_nombres(nombres):
    for i in nombres: print(i)

#imprimir lista de nombres antes y despues de ser modificados
def imprimir_final(magos, copia_magos, cientificos, otros):
    print('-----Magos----- \n')
    for i in copia_magos: print(i)
    print('\n-----Científicos----- \n')
    for i in cientificos: print(i)
    print('\n----Otros---- \n')
    for i in otros: print(i)
    print('\n\n-----Magos Modificado----- \n')
    for i in magos: print(i)
    print('\n')


nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
magos = ['Harry Houdini', 'David Blaine', 'Teller']
copia_magos = magos[:]
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = list(filter(lambda x: (x not in magos) and (x not in cientificos), nombres))



magos = hacer_grandioso(magos)
print('\n\nIMPRIMIR LISTA ORIGINAL\n')
imprimir_nombres(nombres)
print('\nLISTA DE NOMBRES ANTES Y DESPUES DE SER MODIFICADOS \n') 
imprimir_final(magos, copia_magos, cientificos, otros)



