# CUERPO
saldo = 0.0
print("Ingrese meses (N):")
n = int(input())

# CALCULO
i = 1
while i <= n:
    print(f"Aporte mes {i}:")
    aporte = float(input())
    saldo = saldo + aporte
    saldo = saldo + (saldo * 0.008)
    i = i + 1

# RESULTADO
print(f"Saldo final: {saldo}")