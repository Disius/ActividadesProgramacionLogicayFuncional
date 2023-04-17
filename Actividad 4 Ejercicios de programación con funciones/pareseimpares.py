# Lista de numeros donde verifica los pares e impares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Checar si son par e impar
odd = lambda x: x % 2 != 0

even = lambda x: x % 2 == 0

# funcion donde se filtra la suma de los numeros impares
def suma_impares(numeros): 
    return sum(filter(odd, numeros))

# Funcion donde se obtiene el promedio de los numeros pares y agregarlos a una lista, sumar el resultado de la lista    con el tamaño de la misma
def odd_promedio(numeros):
    resultPar = list(filter(even, numeros))
    if len(resultPar) > 0:
        return sum(resultPar) / len(resultPar)
    else: 
        return 0

print("Suma de números impares: ", suma_impares(numbers))
print("Promedio de números pares: ", odd_promedio(numbers))

