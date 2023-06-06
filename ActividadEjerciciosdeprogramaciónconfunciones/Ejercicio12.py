# . Los datos reunidos en la secretaría de industrias relacionado a la producción de N fábricas
# (N𝑁 ≤ 1000) en cada uno de los meses del año anterior, se proporcionan de la siguiente
# forma:
# Haga un programa que calcule lo siguiente:
# a) Los totales anuales de producción de cada fábrica
# b) La clave de la fábrica que más produjo en el año. Indicar también el total de la
# producción.
# c) Imprimir las claves de las fábricascuyas producciones en el mes de julio superaron los
# $3’000,000.00

datos_fabricas = {
    'fab1': [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000],
    'fab2': [150000, 250000, 350000, 450000, 550000, 650000, 750000, 850000, 950000, 1050000, 1150000, 1250000],
    'fab3': [200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000]
}


totales_anuales = {clave: sum(valores) for clave, valores in datos_fabricas.items()}


fabrica_maxima = max(totales_anuales, key=totales_anuales.get)
total_maximo = totales_anuales[fabrica_maxima]


claves_julio = [clave for clave, valores in datos_fabricas.items() if valores[6] > 3000000]


print("Totales anuales de producción:")
for clave, total in totales_anuales.items():
    print(clave, ":", total)

print("Fábrica que más produjo:", fabrica_maxima)
print("Total de producción:", total_maximo)

print("Fábricas con producción en julio superior a $3,000,000.00:", claves_julio)
