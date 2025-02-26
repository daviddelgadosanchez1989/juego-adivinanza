import random



numero_secreto = random.randint(0,100) # El último número no se incluye
cantidad_de_intentos = 0
cantidad_máxima_de_intentos = 7
adivinado = False


print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not cantidad_de_intentos < cantidad_máxima_de_intentos:
        print("Game Over. No has podido adivinar dentro del máximo de intentos")
        break

    entrada = input("Introduce un número del 1 al 99: ") 
    numero = int(entrada)


    if numero == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado, prueba con uno más alto")
    else:
        print("El número es menor al ingresado, prueba con uno más bajo")
    
    cantidad_de_intentos += 1
