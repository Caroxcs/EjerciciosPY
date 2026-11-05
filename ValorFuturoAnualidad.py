# CUERPO
print("Ingrese deposito mensual:")
deposito = float(input())
print("Ingrese tasa (decimal):")
tasa = float(input())
print("Ingrese meses:")
meses = float(input())

# CALCULO
totalDepositado = deposito * meses
vf = deposito * (((1 + tasa)**meses - 1) / tasa)

# RESULTADO
print(f"Total depositado: {totalDepositado}")
print(f"Valor futuro: {vf}")