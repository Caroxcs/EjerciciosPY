# CUERPO
km = float(input("Ingrese los kilometros: "))
noche = input("Esta de noche? (s/n): ")

# CALCULO
base = 2.00 + 1.50 * km
total = base
if km > 10:
    total = total + base * 0.20
if noche == "s":
    total = total + base * 0.30

# RESULTADO
print(f"Tarifa base: {base:.2f}")
print(f"Total a pagar: {total:.2f}")