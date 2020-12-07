"""
   Ejemplo01
   Permitir pagar las mensualidades de las siguientes empresas:
   - Netflix (opción 1) - Disney Plus (opción 2) - Apple TV (opción 3)
   - Amazon Prime (opción 4) El programa es muy particular ya que permite
   pagar 2 o más mensualidades por cada transacción
"""

porcentajeIva1 = 10
porcentajeIva2 = 12
porcentajeIva3 = 14
porcentajeIva4 = 16
Netflix = 10
DisneyPlus = 6
AppleTV = 5
AmazonPrime = 4.50
cadenaFinal = ""

nombre = str(input("Ingrese el nombre del cliente: "))
númeroMeses = int(input("Ingrese el número de mensualidades: "))
empresa = str(input("Ingrese la empresa a la que desea cancelar: "))
print("Introduzca Netflix \Introduzca DisneyPlus \Introduzca AppleTV \Introduzca AmazonPrime")
opcion = str(input("Introduzca aqui su opción: ")
if opción == Netflix:
    impuesto = ((Netflix * porcentajeIva1)/100)
    valorTotal = ((Netflix + impuesto)* 2)
    cadenaFinal = "Nombre: %s\nEmpresa: %s\nNetflix: $ %.2f\nImpuesto: %.2f\n\
ValorTotal: %.2f\n" % (nombre,empresa,Netflix,impuesto,valorTotal)
    print(cadenaFinal)
elif opcion == DisneyPlus:
    impuesto = ((DisneyPlus * porcentajeIva1)/100)
    valorTotal = ((DisneyPlus + impuesto)*2)
    cadenaFinal = "Nombre: %s\nEmpresa: %s\nDisneyPlus: $ %.2f\nImpuesto: %.2f\n\
ValorTotal: %.2f\n" % (nombre,empresa,DisneyPlus,impuesto,valorTotal)
    print(cadenaFinal)
elif opcion == AppleTV:
    impuesto = ((AppleTV * porcentajeIva1)/100)
    valorTotal = ((AppleTV + impuesto)*2)
    cadenaFinal = "Nombre: %s\nEmpresa: %s\nAppleTV: $ %.2f\nImpuesto: %.2f\n\
ValorTotal: %.2f\n" % (nombre,empresa,AppleTV,impuesto,valorTotal)
    print(cadenaFinal)
elif opcion == AmazonPrime:
    impuesto = ((AmazonPrime * porcentajeIva1)/100)
    valorTotal = ((AmazonPrime + impuesto)*2)
    cadenaFinal = "Nombre: %s\nEmpresa: %s\nAmazonPrime: $ %.2f\nImpuesto: %.2f\n\
ValorTotal: %.2f\n" % (nombre,empresa,AmazonPrime,impuesto,valorTotal)
    print(cadenaFinal)
else:
    print("Datos ingresados son incorrectos"
          

    





                
