# Inicializamos las variables que utilizaremos para llevar el control de las ventas
total_ventas = 0
contador_ventas = 0

# Mostramos el menú al usuario
print("Bienvenido al sistema de control de ventas UDES")
print("Por favor, seleccione una opción:")
print("1. Ingresar la ventas del día")
print("2. Imprimir total de las ventas")
print("3. Imprimir el promedio de ventas")
print("4. Salir")
print("5. UDES")

# Utilizamos un ciclo while para que el usuario pueda seleccionar múltiples opciones del menú
while True:
    opcion = input("Ingrese el número de la opción que desea seleccionar: ")        
        
        
    
    # Si el usuario selecciona la opción 1, ingresamos las ventas de un día
    if opcion == "1":
        dia = input("Ingrese el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado o domingo): ")
        ventas = int(input("Ingrese el monto de las ventas para ese día: "))

        # Sumamos las ventas al total y aumentamos el contador en 1
        total_ventas += ventas
        contador_ventas += 1

    # Si el usuario selecciona la opción 2, imprimimos el total de ventas
    elif opcion == "2":
        print("El total de ventas de la semana es: ", total_ventas)

    # Si el usuario selecciona la opción 3, imprimimos el promedio de ventas
    elif opcion == "3":
        # Si no se han ingresado ventas, mostramos un mensaje de error
        if contador_ventas == 0:
            print("Aún no se han ingresado ventas")
        else:
            promedio_ventas = total_ventas / contador_ventas
            print("El promedio de ventas de la semana es: ", promedio_ventas)

    # Si el usuario selecciona la opción 4, salimos del programa
    elif opcion == "4":
        print("***GRACIAS POR PREFERIRNOS***")
        break

    elif opcion == "5" :
        print("Universidad de Santander Campus Cucuta")
        break