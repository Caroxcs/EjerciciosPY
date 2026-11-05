import math
# CUERPO
print("Ingrese cateto 1:")
cat1 = float(input())
print("Ingrese cateto 2:")
cat2 = float(input())

# CALCULO
hip = math.sqrt(cat1**2 + cat2**2)
area = (cat1 * cat2) / 2.0

# RESULTADO
print(f"Hipotenusa: {hip}")
print(f"Area: {area}")