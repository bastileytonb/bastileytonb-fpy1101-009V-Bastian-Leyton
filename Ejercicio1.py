especialistas = 0
residentes = 0

while True:
    try:
        cantidad = int(input("¿Cuántos médicos desea registrar?: "))

        if cantidad > 0:
            break
        else:
            print("Ingrese un número positivo.")

    except:
        print("Ingrese un número válido.")

contador = 1

while contador <= cantidad:

    print("")
    print("Registro médico", contador)

    nombre = input("Ingrese nombre profesional: ")

    while len(nombre) < 6 or " " in nombre:
        print("Nombre inválido.")
        nombre = input("Ingrese nombre profesional: ")

    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia: "))

            if experiencia > 0:
                break
            else:
                print("Ingrese una experiencia válida.")

        except:
            print("Ingrese un número.")

    if experiencia > 5:
        print("Clasificación: Especialista Senior")
        especialistas += 1
    else:
        print("Clasificación: Residente Junior")
        residentes += 1

    contador += 1

print("")
print("= LISTADO FINAL =")
print("Especialistas Senior:", especialistas)
print("Residentes Junior:", residentes)

print("El hospital cuenta con", especialistas,
      "Especialistas Senior y", residentes,
      "Residentes Junior. ¡Sistema listo para operar!")