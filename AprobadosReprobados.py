# CUERPO
aprobados = 0
reprobados = 0
n = int(input("Cantidad de estudiantes: "))
i = 1
while i <= n:
    nota = float(input("Nota del estudiante " + str(i) + ": "))
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    i = i + 1

# RESULTADO
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)