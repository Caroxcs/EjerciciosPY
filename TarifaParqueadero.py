# CUERPO
print("Es estudiante UTPL? (si/no):")
esEstudiante = input()
print("Ingrese las horas de permanencia:")
horas = float(input())

# CALCULO
tarifaBase = horas * 1.00
if esEstudiante == "si":
    tarifaDescontada = tarifaBase * 0.50
    if horas > 4:
        montoFinal = tarifaDescontada * 1.20
    else:
        montoFinal = tarifaDescontada
else:
    tarifaDescontada = tarifaBase
    if horas > 6:
        montoFinal = tarifaDescontada * 1.20
    else:
        montoFinal = tarifaDescontada

# RESULTADO
print(f"El monto a pagar es: ${montoFinal:.2f}")