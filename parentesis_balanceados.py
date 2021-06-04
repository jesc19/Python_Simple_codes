#!/usr/bin/env python
# coding: utf-8

# Escrito por Javier E. Salas Catonga, Abril 2021


'''
Lenguaje de progrmacion: Python 3

GUARDAR EL ARCHIVO COMO: parentesis.py

Compilacion:  dirigirte con la terminal a la ruta donde se encuentra el archivo y tipear la siguiente sentencia: 

              python parentesis.py
'''


#Definimos una función recursiva que llenara los espacios generados con parentesis {}

def Recursive(string, position, n, left, right):
    balanced_chain=''
    if(right == n): 
        for i in string:
            balanced_chain+=i
        print(balanced_chain)
        return
    else:
        if(left > right):
            string[position] = '}'
            Recursive(string, position+1, n,left, right+1)
        if(left < n):
            string[position] = '{'
            Recursive(string, position+1, n, left+1, right)

#Generamos la funcion parentesis

def Parentesis(m):
    spaces = ["",""]*m
    Recursive(spaces, position=0, n=m, left=0, right=0)
    return

#Iteraccion con el usuario

n= int(input('Numero de pares de parentesis:'))
print('Las combinaciones de parentesis balanceados son:')
Parentesis(n)





