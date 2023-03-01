aprobados = 0
reprobados = 0
promedio_notas_finales = 0

while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    p1 = float(input("Ingrese la nota del primer parcial: "))
    p2 = float(input("Ingrese la nota del segundo parcial: "))
    p3 = float(input("Ingrese la nota del tercer parcial: "))
    
    nota_final = (p1 + p2 + p3) / 3
    
    print(f"La nota final de {nombre} es: {nota_final:.2f}")
    
    if nota_final >= 3.0:
        aprobados += 1
    else:
        reprobados += 1
    
    respuesta = input("¿Desea ingresar los datos de otro estudiante? (S/N): ")
    if respuesta.lower() != "s" or "S":
        break

total_estudiantes = aprobados + reprobados

if total_estudiantes > 0:
    promedio_notas_finales = (aprobados * 3.0 + reprobados * 2.0) / total_estudiantes
else:
    print("No se ingresaron datos de ningún estudiante.")

print("Resumen:")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
print(f"Promedio de notas finales: {promedio_notas_finales:.2f}")
