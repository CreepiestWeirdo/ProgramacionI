# Aplicando precedencia resolver las siguientes expresiones


resultado = 5 + 3 * 2 
#           5 +   6 
# resultado = 11
print(resultado)
resultado = 8 / 2 - 3 
#             4   - 3
# resultado = 1
print(resultado)
resultado = 2 ** 3 ** 2 # se resuelve de derecha a izquierda 
#              8   ** 2
# resultado = 512
print(resultado)
resultado = (10 - 3 ) * 2 + 1 
#               7     * 2 + 1
#                  14     + 1 
# resultado = 15
print(resultado)
resultado = not (False or True) and True
#           not      True       and True
#                 False         and True
# resultado = False
print(resultado)
resultado = 4 + 8 // 2 - 3     
#           4 +   4    - 3
# resultado = 5
print(resultado)

