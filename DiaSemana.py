# CUERPO
print("Ingrese un número del 1 al 7 para el día de la semana:")
dia = int(input())

# CALCULO / RESULTADO
match dia:
    case 1 | 2 | 3 | 4 | 5:
        print("Día de clases")
    case 6 | 7:
        print("Fin de semana")
    case _:
        print("Número inválido. Debe ser del 1 al 7.")