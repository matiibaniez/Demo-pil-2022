# concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga 
# Aprende a progamar con _________.

# organizacion = "Haskell"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #f-string

# Mad Libs (Historias Locas)
adj = input('Ingrese un Adjetivo: ')
verbo1 = input('Ingrese un verbo: ')
verbo2 = input('Ingrese un verbo: ')
sustantivo_plural = input('Ingrese un sustantivo_plural: ')

madlib = f" Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con Haskell y alcanza tus {sustantivo_plural}!"

print(madlib)