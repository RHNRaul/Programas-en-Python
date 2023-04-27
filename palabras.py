"""
Crea una función que reciba una cadena y un número entero, y que devuelva una nueva cadena que 
contenga el número de caracteres especificado en el número entero y los tres puntos suspensivos al 
final. Si la cadena original ya es menor que el número entero, devolver la cadena original sin cambios.
"""




import re

def buscarentero(palabra):
    entero = ""
    for i in range(len(palabra)):
        if re.search(r'\d+',palabra[i]):
            entero = entero + palabra[i]
        

    return entero



def regresapalabra(palabra):
    tampalabra= len(buscarentero(palabra))
    entero = int(buscarentero(palabra))
    puntos = "..."
    nuevapalabra = ""
    if (len(palabra)-tampalabra) < entero:
        for i in range(len(palabra)-tampalabra):
            nuevapalabra = nuevapalabra + palabra[i]
    else:
        for i in range(entero):
            nuevapalabra = nuevapalabra + palabra[i]
        nuevapalabra = nuevapalabra + puntos


    return nuevapalabra




palabra = regresapalabra(input("Recibo una palabra y un Entero\n"))    
print(palabra)