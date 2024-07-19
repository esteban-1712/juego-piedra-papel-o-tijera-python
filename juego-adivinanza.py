

from pickle import FALSE
import random


numero_secreto = random.randint(0,100) 
cantidad_intentos = 0
cantidad_max_intentos = 4
adivinado = False


print ("¡Bienvenidos al juego de adivinar el numero secreto!")

while not adivinado:
    if not cantidad_intentos < cantidad_max_intentos:
        print ("¡Game Over! no lo has logrado en la cantidad de intentos maxima")
        break
    numero = int (input("Introduce un numero del 1 al 99: "))

    if numero == numero_secreto:
        print ("Felicitaciones has adivinado el numero secreto")
        adivinado =True
    elif numero < numero_secreto:
        print ("El numero es mayor al ingresado")
    else:
        print ("El numero es menor al ingresado")
    cantidad_intentos += 1

    