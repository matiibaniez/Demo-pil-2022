import random
from re import A
import string


from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual


def obtener_palabra_valida(lista_palabra):
    palabra = random.choice(palabras) #seleccion de palabra al azar
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras) 
    return palabra.upper()


def ahorcado():

    print("===================================")
    print(" Binevenido al juego del ahorcado")
    print("===================================")

    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")


        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("escoge una letra: ").upper()

# Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se ingresaron se agrega al conjunto de letras agregadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas-1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")

        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. por favor elige otra.")
        else:
            print("\nEsta letra no es valida.")
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! Perdiste.")
    else:
        print(f"Adivinaste la palabra {palabra}")

ahorcado()