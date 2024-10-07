
# Ejercicio de laboratorio: Ahorcado

import random

## Ejercicio 1: Implementación de funciones

### Apartado a

def cargar_palabras(ruta):
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
            
        return res

### Apartado b

def elegir_palabra(lista):
    palabra=random.choice(lista)
    return palabra

### Apartado c

def enmascarar_palabra(palabra,letras_probadas):
    palabra_enmascarada=[]
    for letra in palabra:
        if letra in letras_probadas:
            palabra_enmascarada.append(letra)
        else:
            palabra_enmascarada.append("_")
    res = ''.join(palabra_enmascarada)
    return res

### Apartado d

def pedir_letra(letras_probadas):
    nueva_letra = input("Adivina una letra: ")
    while nueva_letra.lower() in letras_probadas:
        nueva_letra = input("Adivina una letra: ")
    return nueva_letra

### Apartado e

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta :
        print('¡Bien hecho! Esa letra está en la palabra.')
        return True
    else:
        print('Lo siento, esa letra no está en la palabra.')
        return False

### Apartado f

def comprobar_palabra_completa(palabra,letras_probadas):
    letras_acertadas=0
    for letra in letras_probadas:
        if letra in palabra:
            letras_acertadas += 1
    if letras_acertadas == len(palabra):
        return True
    else:
        return False

### Apartado g

def ejecutar_turno(palabra_secreta, letras_probadas):
    palabra_enmascarada = enmascarar_palabra(palabra_secreta,letras_probadas)
    print(palabra_enmascarada)
    letra = pedir_letra(letras_probadas)
    comprobacion_letra = comprobar_letra(palabra_secreta,letra)
    if comprobacion_letra == True:
        letras_probadas.add(letra)
        return True
    else:
        return False

## Ejercicio 2: 

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("¡Bienvenido al AHORCADO!")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = set()
    intentos_fallidos = 0
    while True:
        intento = ejecutar_turno(palabra_secreta, letras_probadas)
        if intento == False:
            intentos_fallidos += 1

        if intentos_fallidos == max_intentos:
            print("Has llegado al numero maximo de intentos")
            break

        palabra_terminada = comprobar_palabra_completa(palabra_secreta,letras_probadas)
        if palabra_terminada:
            print("Enhorabuena, has acertado la palabra")
            break

# Iniciar el juego
if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)

