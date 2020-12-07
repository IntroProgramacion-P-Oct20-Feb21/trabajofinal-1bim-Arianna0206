"""
   Ejemplo15
"""
cadenaReporte = ""
bandera = True
sumaEdades = 0
sumaEstaturas = 0.0
contadorIteraciones = 0

cadenaReporte = ("%s%s\n" % (cadenaReporte, "Listado de Jugadores"))
cadenaReporte = ("%s%s\n" % (cadenaReporte, "Listado de Edades"))

while(bandera): 
    nombreJugador = str(input("Ingrese el nombre del Jugador: "))
    posicionCampo = str(input("Ingrese la posición en el campo: "))
    edad = int(input("Ingrese la edad del Jugador: "))
    estatura = float(input("Ingrese la estatura del jugador: "))

    sumaEdades = sumaEdades + edad
    sumaEstaturas = sumaEstaturas + estatura
    contadorIteraciones = contadorIteraciones + 1

    cadenaReporte = ("%s%d.) %s -%s-, edad %d, estatura %.2f\n" % 
    (cadenaReporte, contadorIteraciones,nombreJugador,posicionCampo,edad,estatura)
    cadenaReporte = ("%d\n" % edad)
    
    salir = str(input("Desea salir del cilo; digite: si: "))
    if(salir == "si"): 
        bandera = False

    promedioEdad = float(sumaEdades)/contadorIteraciones
    promedioEstatura = sumaEstaturas/contadorIteraciones

    cadenaReporte = ("%sPromedio de edades: %.2f\n" % (cadenaReporte, promedioEdad))
    cadenaReporte = ("%sPromedio de estaturas: %.2f\n" % (cadenaReporte, promedioEstatura))

print("%s\n" % cadenaReporte)    
