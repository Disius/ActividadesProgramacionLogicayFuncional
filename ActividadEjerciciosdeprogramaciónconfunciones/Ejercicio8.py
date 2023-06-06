# Haga un programa que calcule el número 180 de la secuencia FIBONNACCI. Recuerde que
# los dos primeros números de la serie son 0 y 1. El resto se calcula como la suma de los dos
# números inmediatos que le preceden.
# Ejemplo de la serie: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …,


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


numero_180 = fibonacci(180)
print("El número 180 de la secuencia de Fibonacci es:", numero_180)
