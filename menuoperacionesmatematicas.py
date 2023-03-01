while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 + numero2
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 - numero2
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 * numero2
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 / numero2
        print("El resultado de la división es:", resultado)
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Intente de nuevo.")
