from fractions import Fraction

# Si necesito calular una serie, donde el primer elemento 1 se resta con la fraccion, recibiendo a N en una serie hasta
# que un contador sea igual a N
N = input("Ingresa un valor positivo y entero: ")


def serie(n):
    s = [(-1) ** (i + 1) / i for i in range(1, n + 1)]
    return sum(s)


resultado_serie = serie(int(N))

print(resultado_serie)