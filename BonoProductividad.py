#CUERPO
sueldo = float(input("Ingresar el sueldo base: "))
productividad = float(input("Productividad: "))

if productividad >= 90:
    porcentaje = 20
else:
    if productividad >= 70:
        porcentaje = 10
    else:
        if productividad >= 50:
            porcentaje = 5
        else:
            porcentaje = 0

# CALCULO
bono = sueldo * porcentaje / 100
total = sueldo + bono

# RESULTADO
print(f"Bono: {bono:.2f}")
print(f"Total a pagar: {total:.2f}")