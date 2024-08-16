# for 
# for variable in secuencia:
# #codigo a ejecutar

for i in range(5): # i es el primer numero que incluido y el 5 es el ultimo y esta excluido porque es el corte
    print("Este es el numero ",i)

for _ in range(5): # si la variable no se utiliza en el bloque de codigo del for se utiliza _
    print("Hola!")

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)


# while
# while condicion:

contador = 0 

while contador < 2:
    print("Contador", contador)
    contador += 1

# se evalua while 0 < 2? si
# imprime y suma 1 a contador 0+1
# contador = 1
# se evalua while 1 < 2? si
# imprime y suma 1 a contador 1+1
# contador = 2
# se evalua while 2 < 2? no  

