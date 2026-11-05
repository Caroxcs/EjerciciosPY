# CUERPO
potencia = float(input("Ingrese la potencia (W): "))
horas = float(input("Ingrese las horas de uso diario: "))
tarifa = float(input("La tarifa por kWh: "))

# CALCULO
consumo = (potencia / 1000) * horas * 30
costoEnergia = consumo * tarifa

# RESULTADO
print(f"Consumo mensual es de: {consumo:.2f} kWh")
print(f"El costo total es de: {costoEnergia:.2f}")