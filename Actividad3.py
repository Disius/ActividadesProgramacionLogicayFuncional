# Programa para calcular el dia de la semana


from datetime import date


def calcular_dia_semana(day, month, year):
    day_week = date(year, month, day).weekday()
    # print(day_week)
    days_in_week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    return days_in_week[day_week]


day_in_week = calcular_dia_semana(24, 8, 1999)

print(f'El dia de la semana es {day_in_week} y la fecha es 24-8-1999')
