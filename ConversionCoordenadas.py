import math
# CUERPO
print("Ingrese radio:")
r = float(input())
print("Ingrese angulo en grados:")
theta = float(input())

# CALCULO
rad = math.radians(theta)
x = r * math.cos(rad)
y = r * math.sin(rad)

# RESULTADO
print(f"X: {x}")
print(f"Y: {y}")