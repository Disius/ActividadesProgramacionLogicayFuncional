#  Dado N números enteros como dato en una lista, haga un programa que:
# a) Obtenga cuántos números fueron mayores a cero.
# b) Calcule el promedio de los números positivos.
# c) Obtenga el promedio de todos los números.

lista = []
for i in range(5):
    value = int(input("Ingresa los números enteros: "))
    lista.append(value)


def man_list(lista_it):
    num_int = 0
    suma = 0
    prom = 0
    for n in lista_it:
        if n > 0:
            num_int += 1
            suma += n
            prom = suma / num_int
    prom_all_numbers = sum(lista_it) / len(lista_it)
    return num_int, prom, prom_all_numbers


num = man_list(lista)

print(num)
