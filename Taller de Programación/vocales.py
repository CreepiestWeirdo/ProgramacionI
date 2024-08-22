## Escribe un programa que cuente el numero de vocales en un string 
## proporcionado por el usuario.

texto = input("Ingresar una palabra o texto: ").lower()

vocales = "aeiou"

contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print(f"hay {contador} vocales")