# Realizar un programa que pida al usuario por pantalla un número entero 
# y evalúe si el número es positivo, negativo o cero. Devolver por pantalla el
# resultado:
# "Es positivo" - "Es negativo" - "Es cero"

# SPOILERS 

# pide input al usuario, transforma el dato a entero y lo almacena en la 
# variable numero
numero = int(input("Ingrese un numero entero: ")) 
# evalúa si numero es mayor a cero
if numero > 0:
    print("Es positivo") 
# evalúa si numero es menor a cero
elif numero < 0:
    print("Es negativo")
# el numero es cero
else:
    print("Es cero")