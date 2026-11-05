# CUERPO
viajes = int(input("Viajes por dia: "))
costo = float(input("Costo por viaje: "))
diaSemana = int(input("Dias de la semana que viaja: "))

# CALCULO
gastos = viajes * costo * diaSemana

# RESULTADO
print("Su gasto semanal es de:", gastos)