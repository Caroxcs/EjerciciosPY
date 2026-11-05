# CUERPO
print("Ingrese peso real:")
pesoReal = float(input())
print("Ingrese largo, ancho y alto (presione enter despues de cada uno):")
largo = float(input())
ancho = float(input())
alto = float(input())

# CALCULO
pesoVol = (largo * ancho * alto) / 5000.0
if pesoReal > pesoVol:
    pesoCobrar = pesoReal
else:
    pesoCobrar = pesoVol
costo = pesoCobrar * 2.50

# RESULTADO
print(f"Peso a cobrar: {pesoCobrar}")
print(f"Costo total: ${costo}")