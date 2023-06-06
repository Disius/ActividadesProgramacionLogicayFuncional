sueldos = []

for i in range(5):
    s = int(input("Ingresa el sueldo de tu empleado: "))
    sueldos.append(s)


def aumento_calculo(sueldo):
    if sueldo < 1000:
        aumento = sueldo * 0.15
    else:
        aumento = sueldo * 0.12

    sueldo_nuevo = sueldo + aumento
    return sueldo_nuevo


def imp_sueldo():
    for sueldo in sueldos:
        sueldo_nuevo = aumento_calculo(sueldo)
        print(f"Sueldo anterior: ${sueldo:.2f} --- Nuevo sueldo: ${sueldo_nuevo:.2f}")


imp_sueldo()
nomina_total = sum(map(aumento_calculo, sueldos))

print(f'La nomina total considerando el aumento es: {nomina_total}')
