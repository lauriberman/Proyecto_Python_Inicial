# Proyecto final 
# Python Inicial 

# Autora: Laura Berman 
# Versión: 1.0 

import csv 

from collections import OrderedDict 

# Funciones

# Abrir y leer archivo CSV

def read_csv():

    archivo = 'yeyhousestock.csv' 
    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))


    lista = []
    lista_prendas = []
    lista_talles = []

    # Imprimir lista de marcas para que el usuario ingrese en cual quiere comprar: 

    print('Estas son las marcas que encontrarás en nuestro local:')
    for marca in data: 
        lista.append(marca['MARCA'])

    lista_marcas = list(OrderedDict.fromkeys(lista))
    print(lista_marcas)

    marca_ingresada = input('Ingrese la marca que desea comprar:\n').upper()

    # Chequear si la marca ingresada pertenece al local

    if marca_ingresada in lista_marcas:
        print('Gracias por elegir', marca_ingresada,'! Estas son las prendas que tiene la marca en Yey House:\n')
    else:
        print('La marca ingresada no se encuentra en nuestro local.')
        

    # Si lo está, imprimir las prendas que tenga esa marca en el local
  
    for prenda in data: # Acceder a cada prenda de la lista data
        if prenda['MARCA'] == marca_ingresada:
            #print(prenda) para imprimir la fila entera 
            for k, v in prenda.items():
                if k == 'PRENDA':
                    lista_prendas.append(v)
    
    lista_prendas_ordenada = list(OrderedDict.fromkeys(lista_prendas))
    print(lista_prendas_ordenada)
    
    prenda_elegida = input('Ingrese la prenda que desea comprar:\n').upper()

    if prenda_elegida in lista_prendas_ordenada:
        print('Excelente! Aquí los detalles de la prenda que elegiste:\n')
    else: 
        print('La prenda ingresada no se encuentra disponible.')

    for prenda in data:
        if prenda['PRENDA'] == prenda_elegida:
            print(prenda)

            # por cada fila en la lista 
            # si en la lista prenda se encuentra el nombre de la prenda elegida
            # entonces se imprime la fila en la que esa prenda esta 

    talle_prenda = input('Ingresa el talle en el que deseas comprar tu prenda:\n').upper()

    # Chequear que este disponible el talle ingresado de la prenda elegida: 

    for prenda in data:
        if prenda['PRENDA'] == prenda_elegida:
            for k, v in prenda.items():
                if k == 'TALLE':
                    lista_talles.append(v)

    if talle_prenda in lista_talles:
        print('Perfecto! Tu compra está a un simple paso de ser finalizada!\n')
    else: 
        print('Lo sentimos mucho. La prenda que elegiste no tiene ese talle.')


    

if __name__ == '__main__':
    print('Bienvenidxs a Yey House!')
    read_csv()

    respuesta_usuario = input('Te interesa comprar otro producto?\n').upper()
    
    if respuesta_usuario == 'SI':
        read_csv()

        # Generar un archivo csv nuevo con la confirmacion del/de los producto(s) 
        # comprados por el usuario



