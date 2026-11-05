# CUERPO
suma = 0
print("Ingrese un numero de 3 digitos:")
num = int(input())
original = num

# CALCULO
while num > 0:
    digito = num % 10
    cubo = digito * digito * digito
    suma = suma + cubo
    num = num // 10

# RESULTADO
if suma == original:
    print("Es un numero de Armstrong")
else:
    print("No es un numero de Armstrong")