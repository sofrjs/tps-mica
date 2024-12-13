#1

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
#2
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}")
elif num1 == num2:
    print("Ambos números son iguales")
else:
    print(f"{num2} es mayor a {num1}")
    
#3
n1 = 20
n2 = 3

if n1 % n2 == 0:
    print(f"La división es exacta")
else:
    print(f"El cociente es {n1 // n2}")
    print(f"El resto es {n1 % n2}")

#4
nombre = input("Ingrese su nombre: ")
print(f"Su nombre es: {nombre}")

#5 
nombre1 = str(input("Ingrese su nombre: "))
edad1 = int(input("Ingrese su edad: "))

print(f"Soy {nombre1} y tengo {edad1} años")

#6 convertir grados celsius a kelvin
grados_celsius = int(input("Ingrese una temperatura en Grados Celsius: "))

grados_kelvin = grados_celsius + 273.15

print(f"La temperatura en Grados Kelvin es: {grados_kelvin}")

#7 pasar pesos a dolares
pesos_argentinos = float(input("Ingrese su monto en pesos argentinos: "))

dólares = pesos_argentinos / 1050
print(f"Su monto en dólares es: {dólares}")

#8
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

notas_promedio = int(((nota1 + nota2 + nota3)/3))
print(f"Su promedio es de {notas_promedio}")

if notas_promedio >= 7: 
    print("Alumno aprobado")
elif notas_promedio >= 4:
    print("Alumno regular")
else: 
    print("Alumno desaprobado")