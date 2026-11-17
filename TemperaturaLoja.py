# CUERPO
print("Ingrese la temperatura registrada en Loja (°C):")
temperatura = float(input())

# CALCULO
clasificacion = ""
alerta = ""
if temperatura < 15:
    clasificacion = "Frío"
elif temperatura <= 25:
    clasificacion = "Templado"
else:
    clasificacion = "Cálido"
    if temperatura > 30:
        alerta = "¡Alerta: Calor extremo!"

# RESULTADO
print(f"Clasificación: {clasificacion}")
if alerta != "":
    print(alerta)