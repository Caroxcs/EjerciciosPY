# CUERPO
print("Ingrese promedio:")
prom = float(input())
print("Ingrese asistencia (%):")
asis = float(input())

# CALCULO
if prom >= 9 and asis >= 90:
    cat = "Excelente"
elif prom >= 7 and asis >= 80:
    cat = "Bueno"
elif prom >= 6 and asis >= 70:
    cat = "Regular"
else:
    cat = "Deficiente"

# RESULTADO
print(f"Categoria: {cat}")