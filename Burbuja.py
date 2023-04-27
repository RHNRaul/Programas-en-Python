
"""
Crea una función que ordene una 
lista de números en orden ascendente utilizando 
el algoritmo de burbuja.
"""



def ordenar(Arreglo):
    
    ciclo = True

    while(ciclo):
        contador = 0
        for i in range(len(Arreglo)-1):
            if(Arreglo[i]>Arreglo[i+1]):
                temp = Arreglo[i]
                Arreglo[i] = Arreglo[i+1]
                Arreglo[i+1] = temp
                contador = contador + 1
            else:
                if contador == 0:
                 ciclo = False
    return Arreglo





arreglonumerico=[9,2,1,4,7]
Ordenado = ordenar(arreglonumerico)
print(Ordenado)






