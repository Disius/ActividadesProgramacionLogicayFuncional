# text_input = open(r"C:\Users\defp_\Downloads\correo.txt")

text_input = r"C:\Users\defp_\Downloads\correo.txt"


def dia_semana(text):
    a = open(text)
    lista = []
    for i in a:
        i = i.rstrip()
        if not i.startswith('From '): continue
        words = i.split()
        lista.append(words[2])
    return lista


result = dia_semana(text_input)
print(result)