lista = [2, 6, 7, 5, 7, 8, 10]


def recortar(elementos):
    for i, value in enumerate(elementos):
        if i == 0:
            del elementos[i]
        if i == 5:
            del elementos[i]
    return None


print(f'Resultado de recortar: {recortar(lista)}')


def medio(elementos):
    return elementos


print(f'La nueva lista es: {medio(lista)}')

text_input = open(r"C:\Users\defp_\Downloads\correo.txt")


def words(txt):
    contador = 0
    for linea in txt:
        palabras = linea.split()
        if len(palabras) == 0 or palabras[0] != 0:
            continue
        print(palabras[2])


words(text_input)

inpot = open(r"C:\Users\defp_\OneDrive\Documentos\romeo.txt")


def romeo(txt):
    for text in txt:
        word = text.split()
        print(word)
        for value in word:
            if value in word:
                print(value)
            else:
                print("Estan todas")


romeo(inpot)


def min_max(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    return minimo, maximo


def numeros():
    entrada = input("Ingresa un número (o 'hecho' para terminar): ")
    if entrada == "hecho":
        return []
    else:
        return [int(entrada)] + numeros()


numbers = numeros()
print(f"La lista es: {numbers}")
minimo, maximo = min_max(numbers)

print("El número mínimo es:", minimo)
print("El número máximo es:", maximo)


