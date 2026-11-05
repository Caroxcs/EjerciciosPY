# CUERPO
prestamo = float(input("Ingrese el monto del prestamo: "))
tasa = float(input("Ingrese la tasa mensual: "))
meses = int(input("Ingrese el numero de meses: "))

# CALCULO
interesTotal = prestamo * tasa * meses
cuotaMensual = (prestamo + interesTotal) / meses

# RESULTADO
print(f"La cuota mensual es de: {cuotaMensual:.2f}")
print(f"El interes total es de: {interesTotal:.2f}")