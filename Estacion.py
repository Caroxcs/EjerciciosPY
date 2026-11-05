# CUERPO
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

# CALCULO
f = mes * 100 + dia
if f >= 1221 or f <= 320:
    print("Verano")
else:
    if f <= 620:
        print("Otono")
    else:
        if f <= 922:
            print("Invierno")
        else:
            print("Primavera")