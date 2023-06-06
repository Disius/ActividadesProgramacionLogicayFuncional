# En el centro meteorológico de un país se llevan los promedios mensuales de las lluvias
# caídas en las principales regiones del país. Existen 3 regiones importantes denominadas
# NORTE, CENTRO y SUR. Haga un programa para calcular lo siguiente:
# a) El promedio anual de la región centro.
# b) El mes y registro con menor lluvia en la región sur.
# c) La región con mayor lluvia anual (Considere que los registros anuales de las regiones
# son diferentes)


datos_lluvias = {
    'NORTE': [10, 15, 20, 5, 12, 8, 10, 18, 13, 9, 6, 12],
    'CENTRO': [5, 8, 4, 7, 6, 10, 3, 5, 4, 7, 9, 6],
    'SUR': [(1, 'Enero'), (2, 'Febrero'), (0, 'Marzo'), (3, 'Abril'), (2, 'Mayo'), (1, 'Junio'),
            (2, 'Julio'), (0, 'Agosto'), (1, 'Septiembre'), (0, 'Octubre'), (4, 'Noviembre'), (2, 'Diciembre')]
}


def prom_regi_center(datos):
    d = datos['CENTRO']
    suma = sum(d)
    prom = sum(d) / len(d)
    return prom, suma


imp = prom_regi_center(datos_lluvias)
print(f"El promedio anual de la zona centro es: {format(imp[0], '.2f')}%")


def menor_lluvia_sur(datos):
    a = datos['SUR']
    lista = []
    for i in a:
        if i[0] == 0:
            lista.append(i)
    return lista


data = menor_lluvia_sur(datos_lluvias)
print(f'En los meses de {data[0][1]}, {data[1][1]} y {data[2][1]} ha llovido {data[0][0]} veces')


def reg_mayor_lluvia(datos):
    total_anual_norte = sum(datos['NORTE'])
    total_sur = 0
    sur = datos['SUR']
    for i in sur:
        total_sur += i[0]
    return total_anual_norte, imp[1], total_sur


region_mayor = reg_mayor_lluvia(datos_lluvias)
print(f'La region norte tiene mayor incidencia de lluvia {max(region_mayor)}')