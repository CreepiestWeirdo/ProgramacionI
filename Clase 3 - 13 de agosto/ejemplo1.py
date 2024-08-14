# Evaluar nota de alumno

nota = int(input("Ingrese la nota: "))

if nota >= 90:
    print("Excelente.")
elif 70 <= nota < 90:
    print("Aprobado.")
else:
    print("Desaprobado.")