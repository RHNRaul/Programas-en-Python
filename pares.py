"""
Crea una función que tome una lista de números y 
devuelva una nueva lista que contenga solo los números pares.
"""

def listapares(lista):
    listapar = []
    for i in range(len(lista)-1):
     if int(lista[i])%2 == 0:
        listapar.insert(i,lista[i])  

    return listapar


numeros=[2,4,5,6,1,10,12,14,43,41,51]
lista = listapares(numeros)
print(lista)


