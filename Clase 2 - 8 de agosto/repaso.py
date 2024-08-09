#¿Qué es una Variable?

#Definición: Una variable es un espacio en la memoria del ordenador que se
#  utiliza para almacenar datos que pueden cambiar durante la ejecución de un programa.
#Propósito: Permiten guardar y manipular información como números, texto y 
# otros tipos de datos.


variable = "perro" #cadena de caracteres / string

print(variable)

print (type(variable))

variable = 2 #int / enteros

print(variable)

print (type(variable))

variable = 23.5

print(variable)

print (type(variable))

variable = True #/False

print(variable)

print (type(variable))

# Tipos de datos 'str', 'int', 'float', 'bool'

variable = "Hola Mundo"
print(variable)

print (type(variable))


num1 = 11
num2 = 2
# operadores aritmeticos
# +
aux = num1 + num2
print(aux)
print(type(aux))
# -
aux = num2 - num1
print(aux)
print(type(aux))
# *
aux = num1 * num2
print(aux)
print(type(aux))
# /
aux = num1 / num2
print(aux)
print(type(aux))
# %
aux = num1 % num2
print(aux)
print(type(aux))

# operadores comparacion
# devuelven True o False
dato1 = 10
dato2 = 5
#== es igual
print(dato1 == dato2)
print(dato1 == dato2)
#!= es distinto
print(dato1 != dato2)
# < es menor
print(dato1 < dato2)
# <= es menor o igual
print(dato1 <= dato1)
# > es mayor
print(dato1 > dato2)
# > es mayor o igual
print(dato1 >= dato2)

#operadores logicos
# Y and
# a and b 
# True si todas son verdaderas
# v     v      v
# v     f      f
# f     v      f
# f     f      f
# O or
# a or b
# True si al menos una es verdadera
# v     v      v
# v     f      v
# f     v      v
# f     f      f
# ! not
# si a es True, !a / not a es False
# si a es False, !a / not a es True

# a = tengo un quincho techado
# b = hay sol
# c = comemos asado

# if(a and b)
#    sentencias a ejecutar (c)
# else 
 
#    V   V    V
#
resultado = (2 > 3 or 2 > 4)
#            True       False       
#                  True
print("logica")
print(resultado)
print(type(resultado))

