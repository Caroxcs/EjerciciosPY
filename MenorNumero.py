# CUERPO
print("Ingrese los tres numeros")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))

if a <= b and a <= c:
    menor = a
else:
    if b <= c:
        menor = b
    else:
        menor = c

# RESULTADO
print("El menor de los tres es:", menor)