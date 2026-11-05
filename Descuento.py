# CUERPO
monto = float(input("Monto de la compra: "))

if monto >= 200:
    descuento = monto * 0.15
else:
    if monto >= 100:
        descuento = monto * 0.10
    else:
        descuento = monto * 0.05

# CALCULO
total = monto - descuento

# RESULTADO
print(f"Monto a pagar es: {total:.2f}")