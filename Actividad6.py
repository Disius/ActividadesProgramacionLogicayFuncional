from datetime import date
import calendar


text_input = open(r"C:\Users\defp_\Downloads\correo.txt")


def only_today(text):
    # curr_date = date.today()
    # print(curr_date.weekday())
    # day_name = calendar.day_name[curr_date.weekday()]
    # print(day_name)
    print(text)


only_today(text_input)


# Dia de la semana que se enviaron correos
# for lines in text_input:
#         lines = lines.rstrip()
#         if not lines.startswith("From: "):
#             palabras = lines.split()

#         else:
#             print("Sin correos")
