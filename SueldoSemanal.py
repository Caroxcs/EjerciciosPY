# CUERPO
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Pago por hora: "))

if horas <= 40:
    sueldo = horas * tarifa
else:
    sueldo = (40 * tarifa) + ((horas - 40) * tarifa * 2)

# RESULTADO
print(f"Sueldo semanal: {sueldo:.2f}")