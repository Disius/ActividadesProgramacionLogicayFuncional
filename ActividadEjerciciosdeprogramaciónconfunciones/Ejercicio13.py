# . Un número es perfecto si “la suma de sus divisores excepto el mismo es igual al propio
# número”. Haga un programa para calcular e imprimir los números perfectos menores o
# iguales que N.

def divisores(numero):
    return [x for x in range(1, numero) if numero % x == 0]


def es_perfecto(numero):
    return sum(divisores(numero)) == numero


def numeros_perfectos(N):
    return [x for x in range(1, N + 1) if es_perfecto(x)]


N = int(input("Ingrese el valor de N: "))
resultado = numeros_perfectos(N)
print("Los números perfectos menores o iguales que", N, "son:", resultado)
