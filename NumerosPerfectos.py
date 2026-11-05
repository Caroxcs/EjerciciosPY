# CUERPO
N = int(input("N: "))

suma = 0
for i in range(1, N // 2 + 1):
    if N % i == 0:
        suma = suma + i

# RESULTADO
if N > 1 and suma == N:
    print(N, "es perfecto")
else:
    print(N, "no es perfecto")