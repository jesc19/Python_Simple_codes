#!/usr/bin/env python
# coding: utf-8

#Escrito por Javier E. Salas Catonga, Abril 2021

'''
Lenguaje de progrmacion: Python 3

GUARDAR EL ARCHIVO COMO: substrings.py

Compilacion:  dirigirte con la terminal a la ruta donde se encuentra el archivo y tipear la siguiente sentencia: 

              python substrings.py
'''




#Definimos la función que nos dará los substrings de la cadena y los ordenamos alfabeticamente

import sys

def Nsubstring(string, n):
    
    x=[]
    l=int(len(string))
    for i in range(0,l+1):
        for j in range(i,l+1):
            if(j!=i):
                x.append(string[i:j])
    substrings=sorted(x)
    
    concat=""
    for s in substrings:
        concat+=s
            
    if(n <= 0 or n>len(concat)):
        return sys.exit('Posicion fuera de rango, la posicion maxima es '+str(len(concat)) + ' y la mínima 1')
    else:
        char=concat[n-1]
        return char, concat


#Interaccion con el usuario

cadena=str(input('''Inserte una cadena de caracateres (SIN COMILLAS y SIN ESPACIOS)

ejemplo :  abdc, sjokmmdm, hola, quetal, 89078907, 89787wy7

:'''))

cadena=cadena.replace(" ","")

print("")
n=int(input('Posicion del caracter que se desea conocer (numero entero > 0):'))

result=Nsubstring(cadena, n)

print("")
print('Cadena leida --->', cadena)
print("")
print('Concatenación final ---->', result[1])
print("")
print('Caracter deseado ---->', result[0])
print("")




