# CUERPO
suma = 0.0
print("Ingrese N:")
n = int(input())

# CALCULO
i = 1
while i <= n:
    suma = suma + (1.0 / i)
    i = i + 1

# RESULTADO
print(f"Suma: {suma}")