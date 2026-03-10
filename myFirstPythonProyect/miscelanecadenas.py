def porcentaje(frase, cc=4):
    palabras = frase.split()
    if not palabras:
        return 0, 0
    
    total = len(palabras)
    menores = len(
        [palabra for palabra in palabras if len(palabra) < cc]
    )
    mayores = total - menores

    porc_menores = (menores / total) * 100
    porc_mayores = (mayores / total ) * 100

    return porc_menores, porc_mayores

def histograma(frase):
    vocales = "aeiou"
    contar = {v: frase.lower().count(v) for v in vocales }

    ordenar = sorted(contar.items(), key=lambda x: x[1], reverse=True)

    for vocal, freq in ordenar:
        print(f"{vocal} {freq:2} {'*' * freq}")

def cuatrovocales(frase):
    palabras = frase.lower().split()
    contador_palabras = 0
    vocales = set("aeiou")

    for palabra in palabras:
        vocales_palabras = set(c for c in palabra if c in vocales)
        if len(vocales_palabras) >= 4:
            contador_palabras += 1
    
    return contador_palabras

def cesar(texto, desplazamiento=6):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz,.-¿?="
    resultado = ""
    n = len(alfabeto)

    for char in texto:
        if char in alfabeto:
            cifrado = alfabeto.find(char)
            todo_cifrado = (cifrado + desplazamiento) % n
            resultado += alfabeto[todo_cifrado]
        else:
            resultado += char

    return resultado

def descesar(texto):
    return cesar(texto, desplazamiento=-6)