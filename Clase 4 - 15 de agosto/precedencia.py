# 1- Parentesis ()
# 2- Exponentes ** 
# 3- Multiplicacion / Division / Modulo / Division entera * / % //
# 4- Suma y Resta + -
# 5- Operadores de comparacion < <= >= > == !
# 6- Operadores logicos and or not


resultado = 2 + 3 * 4 
#           2 +   12
# resultado = 14
print(resultado)

resultado = (2 + 3) * 4
#              5    * 4
# resultado = 20
print(resultado)

resultado = 10 - 2 ** 2 + 5 
#           10 - 2 ** 2 + 5
#           10 -  4   + 5 
# resultado = 11    
print(resultado)  

resultado = not 0 and 1 # not False >>> True >>> True y True >>> True
#           True   y  True  >>> True 
print(resultado) 
resultado = not (0 and 1) # True 
#                False y True 
#             not   False
#                   True
print(resultado) 