# CUERPO
saldo = float(input("Capital inicial: "))
deposito = float(input("Deposito mensual: "))
N = int(input("Numero de meses: "))
tasa = float(input("Tasa mensual (%), por ejemplo 1.5: "))

# CALCULO
mes = 1
while mes <= N:
    saldo = saldo + deposito
    saldo = saldo + saldo * tasa / 100
    print(f"Mes {mes}: {saldo:.2f}")
    mes = mes + 1