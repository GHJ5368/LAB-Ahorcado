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