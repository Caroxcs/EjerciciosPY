# CUERPO
print("Ingrese horas:")
horas = float(input())
print("¿Nocturno? (S/N):")
noct = input().strip().upper()

# CALCULO
tarifa = horas * 1.50
if horas > 8:
    tarifa = tarifa * 1.25
if noct == "S":
    tarifa = tarifa * 1.30

# RESULTADO
print(f"Total a pagar: {tarifa}")