# CUERPO
distancia = float(input("Distancia: "))
consumo = float(input("Consumo: "))
precio_combustible = float(input("Precio del combustible por litro: "))
num_peajes = int(input("Numero de peajes: "))
costo_peaje = float(input("Costo unitario del peaje: "))

# CALCULO
litros = distancia / consumo
costo_combustible = litros * precio_combustible
costo_peajes = num_peajes * costo_peaje
total = costo_combustible + costo_peajes

# RESULTADO
print(f"Litros necesarios: {litros:.2f}")
print(f"Costo de combustible: {costo_combustible:.2f}")
print(f"Costo de peajes: {costo_peajes:.2f}")
print(f"Costo total: {total:.2f}")