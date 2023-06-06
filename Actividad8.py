text_input = open(r"C:\Users\defp_\Downloads\correo.txt")
# COMENTE LOS FRAGMENTOS PORQUE NO ME DEJABA USAR LA ENTRADA, FUI REPETITIVO PORQUE NO SUPE LEER LAS LINEAS, ASI QUE LAS CONTE CON EL FOR

# def read_mail_for_day(text):
#     dic = dict()
#     s = []
#     d = []
#     lun = []
#     fri = []
#     for line in text:
#         line = line.rstrip()
#         if not line.startswith("From: "):
#             word = line.split()
#             if word[2] == 'Sat':
#                 s.append(word[2])
#                 dic[word[2]] = len(s)
#             if word[2] == 'Sun':
#                 d.append(word[2])
#                 dic[word[2]] = len(d)
#             if word[2] == 'Mon':
#                 lun.append(word[2])
#                 dic[word[2]] = len(lun)
#             if word[2] == 'Fri':
#                 fri.append(word[2])
#                 dic[word[2]] = len(fri)
#
#     return dic
#
#
# result = read_mail_for_day(text_input)
#
# print(result)


# def read_mail_from_domain(text):
#     for a in text:
#         a = a.rstrip()
#         if a.startswith("From "):
#             palabra = a.split()
#             domain = palabra[1][2:22]
#             print(domain)
#
#
# read_mail_from_domain(text_input)


# def read_mail_from_email(text):
#     dic = dict()
#     d1 = []
#     d2 = []
#     d3 = []
#     d4 = []
#     d5 = []
#     for a in text:
#         a = a.rstrip()
#         if not a.startswith("From: "):
#             palabra = a.split()
#             if palabra[1] == 'gbnango@ittg.edu.mx':
#                 d1.append(palabra[1])
#                 dic[palabra[1]] = len(d1)
#             elif palabra[1] == 'gnango@gmail.com':
#                 d2.append(palabra[1])
#                 dic[palabra[1]] = len(d2)
#             elif palabra[1] == 'galdino.ns@tuxtla.tecnm.mx':
#                 d3.append(palabra[1])
#                 dic[palabra[1]] = len(d3)
#             elif palabra[1] == 'nango.gb@upgch.mx':
#                 d4.append(palabra[1])
#                 dic[palabra[1]] = len(d4)
#             elif palabra[1] == 'aleromi17@hotmail.com':
#                 d5.append(palabra[1])
#                 dic[palabra[1]] = len(d5)
#     print(f'Por EMAIL: {dic}')
#
#
# read_mail_from_email(text_input)
