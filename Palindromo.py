"""
Crea una función que determine si una cadena es un palíndromo 
(es decir, si se lee igual de adelante hacia atrás que de atrás hacia adelante).
"""

def palindromo(palabra):
    tam = (len(palabra) - 1)        

    for i in range(len(palabra)):
        if palabra[i] != palabra[tam]:
            tam=tam-1
            validacion=False 
        else:
            tam=tam-1
            validacion=True
    return validacion





resultado = palindromo(input("ingresa una palabra\n"))
print(resultado)