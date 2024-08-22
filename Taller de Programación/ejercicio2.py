##  Escribe un programa que pida al usuario dos numeros enteros y elija que operacion matematica realizar
## suma / resta / multiplicacion / division / potencia / raiz 

## if - elif - else 

while True:
    # Solicitar los dos números enteros al usuario
    numero1 = int(input("\nIntroduce el primer número entero: "))
    numero2 = int(input("Introduce el segundo número entero: "))

    # Mostrar el menú de opciones
    print("\nSeleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. División")
    print("4. Multiplicación")
    print("5. Potencia")
    print("6. Raíz (del primer número usando el segundo como índice)")
    print("7. Salir")

    # Solicitar la opción al usuario
    opcion = int(input("Introduce el número de la opción deseada: "))

    # Realizar la operación seleccionada
    if opcion == 1:
        resultado = numero1 + numero2
        print(f"\nResultado de la suma: {numero1} + {numero2} = {resultado}")
    elif opcion == 2:
        resultado = numero1 - numero2
        print(f"\nResultado de la resta: {numero1} - {numero2} = {resultado}")
    elif opcion == 3:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"\nResultado de la división: {numero1} / {numero2} = {resultado}")
        else:
            print("\nError: No se puede dividir entre cero.")
    elif opcion == 4:
        resultado = numero1 * numero2
        print(f"\nResultado de la multiplicación: {numero1} * {numero2} = {resultado}")
    elif opcion == 5:
        resultado = numero1 ** numero2
        print(f"\nResultado de la potencia: {numero1} ^ {numero2} = {resultado}")
    elif opcion == 6:
        if numero1 >= 0 and numero2 != 0:
            resultado = numero1 ** (1 / numero2)
            print(f"\nResultado de la raíz de {numero1} con índice {numero2}: {resultado}")
        else:
            print("\nError: No se puede calcular la raíz con índice cero o de un número negativo.")
    elif opcion == 7:
        print("\nGracias por usar la calculadora. ¡Adiós!")
        break
    else:
        print("\nOpción no válida. Por favor, selecciona una opción del 1 al 7.")

    # Preguntar si desea realizar otra operación
    repetir = input("\n¿Deseas realizar otra operación? (si/no): ").strip().lower()
    if repetir != 'si':
        print("\nGracias por usar la calculadora. ¡Adiós!")
        break