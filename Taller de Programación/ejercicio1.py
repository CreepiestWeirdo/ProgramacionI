## Pasar a Python el diagrama de flujo realizado con el siguiente pseudocodigo
## Leer x
## Si x > 10 Entonces
## Si x es par Entonces
## Imprimir "El número es mayor a 10 y es par"
## Sino
## Imprimir "El número es mayor a 10 pero no es par"
## FinSi
## Sino
## Imprimir "El número es menor o igual a 10"
## FinSi

x = int(input("Ingrese un numero: "))

if x > 10:
    if x % 2 == 0:
        print("El numero es mayor a 10 y par")
    else:
        print("El numero es mayor a 10 e impar")
else:
    print("El numero es menor o igual a 10")