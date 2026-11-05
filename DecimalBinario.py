# CUERPO
n = int(input("Ingrese un numero: "))

# CALCULO
b0 = n % 2;  n = n // 2
b1 = n % 2;  n = n // 2
b2 = n % 2;  n = n // 2
b3 = n % 2;  n = n // 2
b4 = n % 2;  n = n // 2
b5 = n % 2;  n = n // 2
b6 = n % 2;  n = n // 2
b7 = n % 2

# RESULTADO
print("El numero en binario es:", str(b7) + str(b6) + str(b5) + str(b4)
       + str(b3) + str(b2) + str(b1) + str(b0))