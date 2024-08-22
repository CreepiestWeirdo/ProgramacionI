## Escribe un programa que solicite 3 numeros al usuario
## y determine cual de ellos es el mayor

num1 = int(input("introduce un num entero: "))
num2 = int(input("introduce otro num entero: "))
num3 = int(input("introduce otro num entero: "))

if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
else:
    mayor = num3

print(f"el numero {mayor} es el mayor")