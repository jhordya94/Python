import math

def menu():
    print("Calcular área y perímetro de figuras geométricas")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Circunferencia")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def area_perimetro_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    area = (base * altura) / 2
    perimetro = base + lado1 + lado2
    print("Área del triángulo: ", area)
    print("Perímetro del triángulo: ", perimetro)

def area_perimetro_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    perimetro = lado * 4
    print("Área del cuadrado: ", area)
    print("Perímetro del cuadrado: ", perimetro)

def area_perimetro_circunferencia():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    print("Área de la circunferencia: ", area)
    print("Perímetro de la circunferencia: ", perimetro)

opcion = menu()

while opcion != 4:
    if opcion == 1:
        area_perimetro_triangulo()
    elif opcion == 2:
        area_perimetro_cuadrado()
    elif opcion == 3:
        area_perimetro_circunferencia()
    else:
        print("Opción no válida")
    
    opcion = menu()

print("Adiós!")
