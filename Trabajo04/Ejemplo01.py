"""
   Ejemplo06
"""

valor1 = int(input("Ingrese el primer valor de la operación: "))
valor2 = int(input("Ingrese el segundo valor de la operación: "))
resultado = 0

print("Introduzca 1 para sumar \Introduzca 2 para restar \Introduzzca 3 para multiplicar: ")

opcion = int(input("Introduzca aqui su opción"))

if opcion == 1:
   resultado = valor1 + valor2

elif opcion == 2:
   resultado = valor1 - valor2

elif opcion == 3:
   resultado = valor1 * valor2

else: 
   print("Operación incorrecta")

print("El resultado de la operación es: %d\n" % resultado) 
