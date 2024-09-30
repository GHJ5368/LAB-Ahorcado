def cargar_palabras(ruta):
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
            
        return res

