"""
   Ejercicio05
   Calcular el pago mensual de un préstamo de 1 año de plazo
"""

monto_Préstamo = float(input("Ingrese el monto del préstamo: "))
interés = float(input("Ingrese el interés mensual a cobrar: "))
número_Meses = float(input("Ingrese el número de meses que consta un año: "))

pago_Mensual = float(monto_Préstamo)*float(interés)*float(número_Meses)

print("el pago mensual de un préstamo es: " + str(pago_Mensual))
