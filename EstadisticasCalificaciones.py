# CUERPO
N = int(input("Cantidad de calificaciones: "))

if N <= 0:
    print("N debe ser mayor que 0")
else:
    suma = 0
    aprobados = 0
    reprobados = 0
    i = 1

    while i <= N:
        nota = float(input("Nota " + str(i) + ": "))
        suma = suma + nota

        if i == 1:
            mayor = nota
            menor = nota
        else:
            if nota > mayor:
                mayor = nota
            if nota < menor:
                menor = nota

        if nota >= 7:
            aprobados = aprobados + 1
        else:
            reprobados = reprobados + 1

        i = i + 1

    print(f"Promedio: {suma / N:.2f}")
    print(f"Mayor: {mayor:.2f}")
    print(f"Menor: {menor:.2f}")
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)