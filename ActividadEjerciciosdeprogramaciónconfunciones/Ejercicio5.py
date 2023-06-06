# En la lista de abajo, se encuentra una serie de ventas que ha realizado un vendedor y
# desea saber cuántas ventas realizó entre:
# a) $0.00 y $200.00
# b) Mayores a $200.00 pero inferiores a $400.00
# c) De $400 en adelante
# 800 320 23 546 123 789 142 567 876 65

lista = [800, 320, 23, 546, 123, 789, 142, 567, 876, 65]


def know(lista_it):
    list_1 = []
    list_2 = []
    list_3 = []
    for i in lista_it:
        if 0 <= i <= 200:
            list_1.append(i)
        if 200 < i < 400:
            list_2.append(i)
        if i > 400:
            list_3.append(i)
    return list_1, list_2, list_3


result = know(lista)
print(f'Ventas en a): {result[0]}')
print(f'Ventas en b): {result[1]}')
print(f'Ventas en c): {result[2]}')
