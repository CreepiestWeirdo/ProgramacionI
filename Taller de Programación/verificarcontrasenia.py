## Escribe un programa que pida al usuario una contraseña y verifique 
## si coincide con una contraseña predefinida.

password = "LApass"

userPass = input("Ingrese su contraseña: ")

if userPass == password:
    print("Bienvenido")
else:
    print("Clave incorrecta")