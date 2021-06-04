#!/usr/bin/env python
# coding: utf-8

#Escrito por Javier E. Salas Catonga, Abril 2021


'''
Lenguaje de progrmacion: Python 3

GUARDAR EL ARCHIVO COMO: superdigito.py

Compilacion:  dirigirte con la terminal a la ruta donde se encuentra el archivo y tipear la siguiente sentencia:

              python superdigito.py
'''




#Definimos la funcion superdigito que hará el bucle de reducir hasta obtener un solo digito
def superdigito(num, nveces):
    x=str(abs(num))
    n=nveces
    superdig=int(x*n)

    while superdig >= 10:
        suma=0
        string=str(superdig)
        l=len(string)
        for i in range(0,l):
            suma+=int(string[i])
        superdig=suma
    else:
        return superdig


#Interaccion con el usuario

numero=int(input('Teclea un numero entero:'))
n=int(input('Concatenar nveces:'))
print("")
print("Numero leido --->", str(abs(numero))*n)
print("")
print("El superdigito es:" , superdigito(numero,n))
print("")



