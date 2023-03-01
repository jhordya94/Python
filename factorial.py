def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un número para calcular: "))

factorial = calcular_factorial(numero)
print("El factorial de ", numero, " es: ", factorial)

numeros_pares = 0
numeros_impares = 0
acumulado_pares = 0
acumulado_impares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        numeros_pares += 1
        acumulado_pares += i
    else:
        numeros_impares += 1
        acumulado_impares += i

print("Cantidad de números pares: ", numeros_pares)
print("Cantidad de números impares: ", numeros_impares)
print("Valor acumulado de los pares: ", acumulado_pares)
print("Valor acumulado de los impares: ", acumulado_impares)
