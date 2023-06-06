# Haga un programa para calcular lo que hay que pagar por un conjunto de llamadas
# telefónicas. Por cada llamada se ingresa el tipo (Internacional, Nacional, Local) y la duración
# en minutos. El criterio que se sigue para calcular el costo de cada llamada es el siguiente:
# Internacional: 3 primeros minutos $7.59
# Cada minuto adicional $3.03
# Nacional: 3 primeros minutos $1.20
# Cada minuto adicional $0.48
# Local: Las primeras 50 llamadas no se cobran.
# Cada llamada adicional cuesta $0.60


def calcular_costo_llamada(tipo, duracion):
    if tipo == "Internacional":
        primeros_minutos = min(duracion, 3)
        minutos_adicionales = max(duracion - 3, 0)
        costo = primeros_minutos * 7.59 + minutos_adicionales * 3.03
    elif tipo == "Nacional":
        primeros_minutos = min(duracion, 3)
        minutos_adicionales = max(duracion - 3, 0)
        costo = primeros_minutos * 1.20 + minutos_adicionales * 0.48
    else:
        costo = 0.60 if duracion > 50 else 0

    return costo


llamadas = [("Nacional", 2), ("Local", 60), ("Internacional", 10)]
costos = map(lambda llamada: calcular_costo_llamada(llamada[0], llamada[1]), llamadas)
costo_total = sum(costos)

print(f'El costo total de las llamadas es: {costo_total}')