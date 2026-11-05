import math
# CUERPO
x1 = float(input("Ingrese el valor de x1: "))
x2 = float(input("Ingrese el valor de x2: "))
y1 = float(input("Ingrese el valor de y1: "))
y2 = float(input("Ingrese el valor de y2: "))

# CALCULO
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
pMedio_x = (x1 + x2) / 2
pMedio_y = (y1 + y2) / 2

# RESULTADO
print(f"La distancia entre los dos puntos es: {distancia:.2f}")
print(f"El punto medio es: ({pMedio_x:.2f}, {pMedio_y:.2f})")