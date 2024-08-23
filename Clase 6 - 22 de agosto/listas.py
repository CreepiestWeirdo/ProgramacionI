# Lista> coleccion ordenada de elementos que pueden ser de cualquier tipo de datos.

mi_lista = [1, 2, 3, 4, 5, 2, 4, 1]

# Caracteristicas> 
# son mutables, los elementos pueden modificados
# pueden contener elementos de distintos tipos de datos
# soportan duplicados 

frutas = ["manzana", "banana", "cereza", "pera", "naranja"]

print(frutas)

print(frutas[1]) # acceso de datos por indexacion, entre corchetes se cita el indice

print(type(frutas))
print(type(frutas[2]))

print(frutas[2])
print(frutas[-1])
print(frutas[1 : 4]) #slicing
print(frutas[1 : -1]) 


#TAREA PARA EL MARTES, RECORRER LA LISTA CON FOR 
for fruta in frutas:

    while i < 4:
        print(frutas[i])
        i += 1
