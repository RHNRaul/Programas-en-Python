"""
Crea una función que calcule el factorial de un número entero utilizando un ciclo while.
"""
def factorial(numero):
    
    factorial = 1

    while(numero > 0):
        factorial = factorial * numero    
        numero = numero - 1

    return factorial;



resultado = factorial(int(input("ingrese un numero\n")))
print(resultado)



