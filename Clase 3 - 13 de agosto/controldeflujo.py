# if-else 
# if se evalúa una condición y si verdadera se ejecuta el bloque de código dentro del if.
edad = 12

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("No eres mayor de edad.")

# operadores de comparación
# == igual que
# != distinto que 
# > mayor que
# >= mayor o igual que 
# < menor que 
# <= menor o igual que 
# 
# devuelve tipo de dato booleano True / False

# operadores lógicos
# and si todo es verdadero es True
# or si al menos una condición se cumple es True
# not devuelve la condición de verdad opuesta

a = 40
b = 20
c = 30

if a < b and b < c:
    print("a es menor que b y b es menor que c")
elif not(a > c):
    print("a no es mayor que c")
else:
    print("a es mayor")

