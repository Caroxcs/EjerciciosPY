# CUERPO
suma = 0
n = int(input("Total de notas que va a ingresar: "))
i = 1
while i <= n:
    nota = float(input("Nota " + str(i) + ": "))
    suma = suma + nota
    i = i + 1

# CALCULO
promedio = suma / n

# RESULTADO
print(f"El promedio es: {promedio:.2f}")