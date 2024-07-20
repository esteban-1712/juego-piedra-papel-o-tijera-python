nombre_jugador1 = input("Por favor ingrese el nombre del primer jugador: ")
nombre_jugador2 = input ("Por favor ingrese el nombre del segundo jugador: ")
eleccion_1 = input(f"Por favor {nombre_jugador1} ingrese su eleccion: ").lower()
eleccion_2 = input (f"Pr favor {nombre_jugador2} ingrese su eleccion: ").lower()
condicion1 = eleccion_1 == "piedra" and eleccion_2 == "tijera"
condicion2 = eleccion_1 == "papel" and eleccion_2 == "piedra"
condicion3 = eleccion_1 == "tijera" and eleccion_2 == "papel" 

if condicion1 or condicion2 or condicion3:
    print (f"El ganador es el jugador {nombre_jugador1}")
else:
    print (f"el ganador es el jugador {nombre_jugador2}")
