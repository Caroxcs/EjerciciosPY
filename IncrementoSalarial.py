# CUERPO
salario = 1500
anual = 1
while anual <= 6:
    salario = salario * 1.10
    print(f"Anio {anual}: ${salario:.2f}")
    anual = anual + 1

# RESULTADO
print(f"Salario final despues de 6 anios: ${salario:.2f}")