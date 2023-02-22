def esBisiesto(year):
    if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    
# esBisiesto(2023)
esBisiesto(2024)

