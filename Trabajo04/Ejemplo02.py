"""
   Ejemplo07
"""

valor1 = int(input("Ingrese el primer valor de la operación: "))
valor2 = int(input("Ingrese el segundo valor de la operación: "))
resultado = 0
tipo = ""

print("Introduzca 1 para sumar \Introduzca 2 para restar \Introduzzca 3 para multiplicación")

opcion = int(input("Introduzca aqui su opción: "))

if opcion == 1:
   resultado = valor1 + valor2
   tipo = suma

elif opcion == 2:
   resultado = valor1 - valor2
   tipo = resta

elif opcion == 3:
   resultado = valor1 * valor2
   tipo = multiplicación

else: 
   print("Operación incorrecta")

print("El resultado de la operación %s es: %d\n" % (tipo,resultado)) 