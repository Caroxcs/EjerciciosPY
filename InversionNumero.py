# CUERPO
inv = 0
print("Ingrese numero:")
num = int(input())

# CALCULO
while num > 0:
    dig = num % 10
    inv = (inv * 10) + dig
    num = num // 10

# RESULTADO
print(f"Invertido: {inv}")