import random

def cargar_palabras(ruta):
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
            
        return res

def elegir_palabra(lista):
    palabra=random.choice(lista)
    return palabra

def enmascarar_palabra(palabra,letras_probadas):
    palabra_enmascarada=[]
    res=""
    for letra in palabra:
        if letra in letras_probadas:
            palabra_enmascarada.append(letra)
        else:
            palabra_enmascarada.append("_")
    res = ''.join(palabra_enmascarada)
    return res

def pedir_letra(letras_probadas):
    nueva_letra = input("Dime una nueva letra: ")
    while nueva_letra in letras_probadas:
        nueva_letra = input("Dime una nueva letra: ")
        nueva_letra.lower()
    return nueva_letra

def comprobar_letra(palabra_secreta, letra):
    if letra in palabra_secreta :
        return True
    else:
        return False

def comprobar_palabra_completa(palabra,letras_probadas):
    letras_acertadas=0
    for letra in letras_probadas:
        if letra in palabra:
            letras_acertadas += 1
    if letras_acertadas == len(palabra):
        return True
    else:
        return False

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
