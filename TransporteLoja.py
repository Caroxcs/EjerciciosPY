# CUERPO
print("--- TRANSPORTE EN LOJA (5 km) ---")
print("1 = Bus urbano")
print("2 = Taxi")
print("3 = Bicicleta")
print("4 = Caminar")
print("Elija una opción:")
opcion = int(input())

# CALCULO / RESULTADO
match opcion:
    case 1:
        print("Tiempo estimado: 25-35 minutos.")
        print("Comentario: Económico, pero depende de las rutas urbanas.")
    case 2:
        print("Tiempo estimado: 10-15 minutos.")
        print("Comentario: Rápido y directo, ideal para llegar a tiempo.")
    case 3:
        print("Tiempo estimado: 20-25 minutos.")
        print("Comentario: Excelente opción ecológica, requiere esfuerzo por las cuestas.")
    case 4:
        print("Tiempo estimado: 60-75 minutos.")
        print("Comentario: Ejercicio saludable, aunque toma considerable tiempo.")
    case _:
        print("Opción de transporte no válida.")