# En un país en algún lado de la galaxia:
# mayores de 18 pueden conducir y votar 
# mayores de 16 pueden votar pero no conducir 
# menores de 16 no pueden votar ni conducir. 
# Hacer un programa que le pregunte al usuario su edad y luego de la 
# evaluación de las condiciones le informe sus permisos.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Puedes votar y conducir")
elif edad >= 16: 
    print("Puedes conducir pero no votar")
else:
    print("No puedes votar ni conducir")