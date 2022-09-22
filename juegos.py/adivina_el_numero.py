import random


def adivina_el_numero(x):
    print("----------------------")
    print(" Bienvenido al juego! ")
    print("----------------------")
    print("Tu meta es adivinar el numero generado por la computadora.")

    numero_aleatorio = random.randint(1, x) # Numero aleatorio entre 1 y x.

    prediccion = 0 # Para que sea distinto de el numero aleatorio.

    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #f-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")

        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande.")
        
    print(f"Felicitaciones! adivinaste el numero {numero_aleatorio} correctamente.")


adivina_el_numero(10)



