# . Lo siguiente se llama la conjetura de ULAM en honor del matemático S. Ulam:
# • Comience con cualquier entero positivo
# • Si es par, divídalo entre 2; si es impar, multiplíquelo por 3 y agréguele 1.
# • Obtenga enteros sucesivamente repitiendo el proceso.
# Al final, obtenga el número 1, independientemente del entero inicial. Por ejemplo, cuando
# el entero inicial es 26, la secuencia será: 26, 13,40, 20, 10, 5, 16, 8, 4, 2, 1.
# Construya un programa que lea un entero positivo y obtenga e imprima la sucesión de
# ULAM.

s = int(input("Ingresa un numero positivo: "))
lista = [s]


def ULAM(number):
    if number % 2 == 0:
        e = number / 2
        lista.append(e)
        if e > 2:
            ULAM(e)
        else:
            lista.append(1)
    elif number % 2 != 0:
        o = number * 3 + 1
        lista.append(o)
        if o > 2:
            ULAM(o)


print(ULAM(s))
print(lista)
