a = float(input("Angulo 1: "))
b = float(input("Angulo 2: "))
c = float(input("Angulo 3: "))

# CUERPO
if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
    print("No forman un triangulo")
else:
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    if mayor < 90:
        print("Acutangulo")
    else:
        if mayor == 90:
            print("Rectangulo")
        else:
            print("Obtusangulo")