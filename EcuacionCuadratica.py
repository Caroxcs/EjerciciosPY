# CUERPO
print("Ingrese a, b, c (presione enter despues de cada uno):")
a = float(input())
b = float(input())
c = float(input())

# CALCULO
disc = (b * b) - (4 * a * c)
if disc > 0:
    msj = "Dos soluciones reales"
elif disc == 0:
    msj = "Una solucion real"
else:
    msj = "Ninguna solucion real"

# RESULTADO
print(msj)