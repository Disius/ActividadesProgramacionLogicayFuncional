# Escriba un programa que lea un número entero N y calcule la suma de la siguiente serie:
# 1
# 1 + 2
# 2 + 3
# 3 + ⋯ 𝑁
#

s = int(input("Ingresa un número positivo entero: "))
lista = []


def serie(a):
    exp = pow(a, a)
    lista.append(exp)
    if a < 30:
        b = a + 1
        serie(b)
    else:
        suma = sum(lista)
        print(f'La suma de la serie es: {suma}')


serie(s)
print(f'Serie: {lista}')
