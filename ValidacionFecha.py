# CUERPO
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Anio: "))

valida = True
maxdia = 31

# CALCULO
if mes < 1 or mes > 12 or anio < 1 or dia < 1:
    valida = False
else:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        maxdia = 30
    else:
        if mes == 2:
            if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
                maxdia = 29
            else:
                maxdia = 28
    if dia > maxdia:
        valida = False

# RESULTADOS
if valida:
    print("Fecha valida")
else:
    print("Fecha invalida")