stock = 120
prestamos = 0
historial = 0
opcion = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while opcion != 5:

    print("")
    print("=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            print("Libros disponibles:", stock)

        elif opcion == 2:

            cantidad = int(input("Cantidad de libros a prestar: "))



            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")

            elif cantidad > stock:
                print("No hay suficientes libros disponibles.")

            else:
                stock -= cantidad
                prestamos += cantidad
                historial += cantidad

                print("Préstamo realizado.")

        elif opcion == 3:

            cantidad = int(input("Cantidad de libros a devolver: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")

            elif cantidad >= prestamos:
                print("No puede devolver más libros de los prestados.")

            else:
                stock += cantidad
                prestamos -= cantidad

                print("Devolución realizada.")

        elif opcion == 4:
            print("")
            print("=== HISTORIAL ===")
            print("Préstamos activos:", prestamos)
            print("Total de préstamos:", historial)

        elif opcion == 5:

            print("Gracias por utilizar nuestro software, hasta la próxima.")

        else:

            print("Opción no válida.")

    except:

        print("Ingrese un número válido.")
    