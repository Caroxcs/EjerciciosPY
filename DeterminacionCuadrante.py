# CUERPO
print("Ingrese x e y (presione enter despues de cada uno):")
x = float(input())
y = float(input())

# CALCULO
if x == 0 and y == 0:
    pos = "Origen"
elif x == 0:
    pos = "Eje Y"
elif y == 0:
    pos = "Eje X"
elif x > 0 and y > 0:
    pos = "Cuadrante I"
elif x < 0 and y > 0:
    pos = "Cuadrante II"
elif x < 0 and y < 0:
    pos = "Cuadrante III"
else:
    pos = "Cuadrante IV"

# RESULTADO
print(pos)