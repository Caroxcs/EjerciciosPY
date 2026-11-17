# CUERPO
print("--- MENÚ CAFETERÍA UTPL ---")
print("1 = Café ($1.50)")
print("2 = Jugo ($1.20)")
print("3 = Sandwich ($2.50)")
print("4 = Salir")
print("Seleccione una opción:")
opcion = int(input())

# CALCULO / RESULTADO
match opcion:
    case 1:
        print("Producto: Café. Precio: $1.50")
    case 2:
        print("Producto: Jugo. Precio: $1.20")
    case 3:
        print("Producto: Sandwich. Precio: $2.50")
    case 4:
        print("¡Gracias por su visita! Saliendo...")
    case _:
        print("Opción inválida.")