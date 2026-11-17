# CUERPO
print("--- CONVERSOR ---")
print("1 = Kilómetros a metros")
print("2 = Metros a centímetros")
print("3 = Horas a minutos")
print("4 = Salir")
print("Seleccione una opción:")
opcion = int(input())

valor = 0.0
if 1 <= opcion <= 3:
    print("Ingrese el valor a convertir:")
    valor = float(input())

# CALCULO
resultado = 0.0
match opcion:
    case 1:
        resultado = valor * 1000
        print(f"Resultado: {resultado} metros")
    case 2:
        resultado = valor * 100
        print(f"Resultado: {resultado} centímetros")
    case 3:
        resultado = valor * 60
        print(f"Resultado: {resultado} minutos")
    case 4:
        print("Saliendo del conversor...")
    case _:
        print("Opción inválida.")