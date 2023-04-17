# Lista de numeros donde verifica los pares e impares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Checar si son par e impar
odd = lambda x: x % 2 != 0

even = lambda x: x % 2 == 0

# Filtrar la suma de los numeros impares
def suma_impares(numeros): 
    return sum(filter(odd, numeros))
# suma_impares = sum(filter(odd, numbers))

# Filtrar los numeros pares y agregarlos a una lista
resultPar = list(filter(even, numbers))

# si el tamaño de resultadoPar es mayor que 0 entonces sumara los numero pares y lo dividira por el tamaño de la lista
 
if len(resultPar) > 0:
    promedio = sum(resultPar) / len(resultPar)
else: 
    promedio = 0

print("Suma de números impares: ", suma_impares(numbers))
print("Promedio de números pares: ", promedio)

