"""
   Ejemplo01
"""
cadenaReporte = ""
cadenaReporte1 = ""
cadenaReporte2 = ""
cadenaEdades = ""
bandera = True
sumaEdades = 0
sumaEstaturas = 0.0
contadorIteraciones = 0
 
cadenaReporte1 = ("%s%s\n" % (cadenaReporte,"Listado de Jugadores"))



while(bandera): 
    nombreJugador = str(input("Ingrese el nombre del Jugador: "))
    posicionCampo = str(input("Ingrese la posición en el campo: "))
    edad = int(input("Ingrese la edad del Jugador: "))
    estatura = float(input("Ingrese la estatura del Jugador: "))
    cadenaReporte2 = ("%s%s\n" % (cadenaReporte2,"Listado de Edades"))

    sumaEdades = sumaEdades + edad
    sumaEstaturas = sumaEstaturas + estatura
    contadorIteraciones = contadorIteraciones + 1

    cadenaReporte1 = ("%s%d.) %s -%s- , edad %d, estatura %.2f\n" %
    (cadenaReporte,contadorIteraciones, nombreJugador, posicionCampo,edad,estatura))
    

    salir = str(input("Desea salir del ciclo; digite: si : "))
    if(salir == "si"):
      bandera = False
      promedioEdad = (float(sumaEdades)/contadorIteraciones)
      promedioEstatura = (sumaEstaturas/contadorIteraciones)

      cadenaReporte = ("%sPromedio de esdades: %.2f\n" % (cadenaReporte,promedioEdad))

      cadenaReporte = ("%sPromedio de estaturas: %.2f\n" % (cadenaReporte, promedioEstatura))

print("%s\n%s\n%s\n" % (cadenaReporte1,cadenaReporte2,cadenaReporte)