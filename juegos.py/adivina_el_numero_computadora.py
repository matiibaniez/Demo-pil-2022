import random


def adivina_el_numero_computadora(x):
    
    print("----------------------")
    print(" Bienvenido al juego! ")
    print("----------------------")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo.")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""
    while respuesta != "c":
        # Generar una prediccion
        if limite_inferior != limite_superior: 
            prediccion = random.randint(limite_inferior,limite_superior)
        else: 
            prediccion = limite_inferior # Tambien podria ser el limite superior.
        # Obtener respuesta de usuario
        respuesta = input(f" Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B).Si es correcta, ingresa (c): ").lower()

        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    print(f"Sii! La computadora adivino tu numero correctamente: {prediccion} ")


adivina_el_numero_computadora(10)

# Esto hace la computadora
# Intervalo inicial: [1,10]
# Prediccion: 6
# Respuesta: "a"
# Intervalo: [1,5]