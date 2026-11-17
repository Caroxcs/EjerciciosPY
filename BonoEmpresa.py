# CUERPO
print("Ingrese los años de antigüedad:")
antiguedad = int(input())
print("Ingrese el sueldo:")
sueldo = float(input())
print("La evaluación es excelente? (si/no):")
evaluacionExcelente = input()

# CALCULO
porcentajeBono = 0.0
if antiguedad > 2:
    if evaluacionExcelente == "si":
        porcentajeBono = 0.15
    else:
        porcentajeBono = 0.10
else:
    if evaluacionExcelente == "si":
        porcentajeBono = 0.05
    else:
        porcentajeBono = 0.0

bono = sueldo * porcentajeBono
sueldoTotal = sueldo + bono

# RESULTADO
print(f"Bono calculado: ${bono:.2f}")
print(f"Sueldo total a pagar: ${sueldoTotal:.2f}")