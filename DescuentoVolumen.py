# CUERPO
print("Ingrese monto:")
monto = float(input())
print("Frecuente (S/N):")
frec = input().strip().upper()

# CALCULO
if monto >= 500:
    base = 15
elif monto >= 300:
    base = 10
elif monto >= 100:
    base = 5
else:
    base = 0

if frec == "S":
    dcto = base + 5
else:
    dcto = base

total = monto - (monto * dcto / 100.0)

# RESULTADO
print(f"Total a pagar: {total}")