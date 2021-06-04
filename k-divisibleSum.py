#!/usr/bin/env python
# coding: utf-8

# In[2]:


#impostamos herramientas
from itertools import product

#Damos los valores

#Cuando damos valores como k=8 toma algo de tiempo ya que hace todas las combinaciones de arreglos (nota:necesita mejorar el tiempo)

n=4
k=3

#Creamos un arreglo de listas de las posibles combinaciones de enteros
list_integers=[]
for i in range(1,k+1):
    list_integers.append(i)

lista = list(product(list_integers, repeat=n))

#Evaluamos si la suma de los elementos de la lista es multiplo de k
for comb in lista:
    sum=0
    for j in comb:
        sum+=j
    
    #Imprimimos el maximo minimo posible    
    if (sum%k==0):
        print('arreglo:',list(comb))
        print('la suma es', sum, 'y es multiplo de', k)
        print('el maximo minimo posible es',max(comb))
        print('')
        

