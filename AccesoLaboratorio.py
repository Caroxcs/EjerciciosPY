# CUERPO
print("Es estudiante? (si/no):")
esEstudiante = input()

# CALCULO
resultado = ""
if esEstudiante == "si":
    print("Tiene carné vigente? (si/no):")
    tieneCarne = input()
    if tieneCarne == "si":
        resultado = "Acceso permitido"
    else:
        resultado = "Acceso denegado (Carné no vigente)"
else:
    print("Tiene autorización especial del docente? (si/no):")
    tieneAutorizacion = input()
    if tieneAutorizacion == "si":
        resultado = "Ingreso temporal"
    else:
        resultado = "Acceso denegado"

# RESULTADO
print(f"Resultado: {resultado}")