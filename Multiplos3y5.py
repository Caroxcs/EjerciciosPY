# CUERPO
cont = 0
suma = 0
print("Ingrese N:")
n = int(input())

# CALCULO
i = 1
while i <= n:
    if i % 3 == 0 or i % 5 == 0:
        cont = cont + 1
        suma = suma + i
    i = i + 1

# RESULTADO
print(f"Cantidad: {cont} Suma: {suma}")