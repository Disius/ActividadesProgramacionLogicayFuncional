from functools import reduce

def calcular_total_por_tipo(vinos):
    return list(map(sum, zip(*vinos)))

def calcular_total_por_anio(vinos):
    return list(map(sum, vinos))

def obtener_anio_max_cantidad(vinos):
    max_cantidad = max(reduce(lambda x, y: x + y, vinos))
    anio_max_cantidad = vinos.index(list(filter(lambda x: sum(x) == max_cantidad, vinos))[0]) + 1
    return (anio_max_cantidad, max_cantidad)

def verificar_no_produccion_tipo(vinos, tipo):
    for i, anio in enumerate(vinos):
        if anio[tipo - 1] == 0:
            return i + 1
    return None


vinos = [
    [100, 200, 150, 50, 75],
    [120, 180, 160, 60, 80],
    [90, 220, 140, 70, 85]
]

total_por_tipo = calcular_total_por_tipo(vinos)
print("Total producido por tipo de vino:", total_por_tipo)

total_por_anio = calcular_total_por_anio(vinos)
print("Total producido por año:", total_por_anio)

anio_max_cantidad = obtener_anio_max_cantidad(vinos)
print("Año con mayor cantidad de litros de vino:", anio_max_cantidad)

anio_no_produccion = verificar_no_produccion_tipo(vinos, 3)

if anio_no_produccion:
    print("Año en que no se produjo el vino tipo 3:", anio_no_produccion)
else:
    print("No hubo ningún año sin producción del vino tipo 3.")