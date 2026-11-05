# CUERPO
num = int(input("Ingrese un numero decimal entero: "))

if num == 0:
    hex = "0"
else:
    hex = ""
    while num > 0:
        residuo = num % 16
        if residuo < 10:
            digito = str(residuo)
        else:
            if residuo == 10:
                digito = "A"
            elif residuo == 11:
                digito = "B"
            elif residuo == 12:
                digito = "C"
            elif residuo == 13:
                digito = "D"
            elif residuo == 14:
                digito = "E"
            else:
                digito = "F"
        hex = digito + hex
        num = num // 16

print("El numero en hexadecimal es:", hex)