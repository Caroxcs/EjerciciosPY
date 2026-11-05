# CUERPO
precio = float(input("Ingrese el precio original: "))

# CALCULO
conDescuento = precio * 0.80
iva = conDescuento * 0.15
precioFinal = conDescuento + iva

# RESULTADO
print("Precio con descuento:", conDescuento)
print("Precio final:", precioFinal)