# CUERPO
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

# CALCULO
while b != 0:
    residuo = a % b
    a = b
    b = residuo

# RESULTADO
print("El maximo comun divisor es:", a)