# CUERPO
print("Ingrese capital:")
cap = float(input())
print("Ingrese tasa:")
tasa = float(input())
print("Ingrese meses:")
meses = float(input())

# CALCULO
intTotal = cap * tasa * (meses / 12.0)
cuota = (cap + intTotal) / meses

# RESULTADO
print(f"Interes: {intTotal}")
print(f"Cuota: {cuota}")