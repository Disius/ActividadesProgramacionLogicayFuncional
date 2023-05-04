def redondeo(chicles, cerillos, jabon):
    totalChicles = 0.80 * chicles
    totalCerillos = 1.26 * cerillos
    totalJabon = 18.45 * jabon
    total = [totalChicles, totalCerillos, totalJabon]

    subtotal = sum(total)
    print("Total de los productos: $", subtotal)

    iva = (subtotal * 0.16) + subtotal
    print("Total con IVA: $", iva)

    redondeado = round(iva)

    print("Total redondeado: $", redondeado)


redondeo(7, 3, 5)

# Una persona compra en una tienda los siguientes articulos
# 7 chicles a 0.80 centavos cada uno
# 3 cajas de cerillos a 1.26 cada uno
# 5 kilos de jabon a 18.45 cada uno