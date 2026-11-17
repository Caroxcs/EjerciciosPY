# CUERPO
print("Es estudiante UTPL? (si/no):")
esEstudiante = input()
print("Ingrese el monto de compra:")
monto = float(input())

# CALCULO
descuento = 0.0
if esEstudiante == "si":
    if monto > 30:
        descuento = 0.25
    else:
        descuento = 0.20
else:
    if monto > 50:
        descuento = 0.10
    else:
        descuento = 0.0

montoFinal = monto - (monto * descuento)

# RESULTADO
print(f"El monto final a pagar es: ${montoFinal:.2f}")