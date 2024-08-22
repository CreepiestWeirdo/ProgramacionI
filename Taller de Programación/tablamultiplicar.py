## Escribe un programa que genere la tabla de multiplicar de un numero ingresado 
## por el usuario, desde 1 hasta 10.

numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))

#Generar tabla de multiplicar
#print(f"Tabla de multiplicar del {numero}:")
for num in range(1, 11):
    print(f"{numero} x {num} = {numero * num}")

