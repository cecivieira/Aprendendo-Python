#coding=utf-8
#8. Realiza una función que descarge el libro "ALICE'S ADVENTURES IN WONDERLAND" de
# "http://www.gutenberg.org/files/11/11-0.txt" vuelque su contenido en un string, elimine caràcteres especiales
# ('\r.,!:@#$?\''), convierta letras mayúsculas a minúsculas, y muestre entonces las n palabras (pasado por parámetro)
# más comunes.

def n_palabras(x):
    import urllib2
    import string

    archivo = urllib2.urlopen(x)
    libro = open("alice.txt", "w")
    libro.write(archivo.read())
    libro.close()

    libro = open("alice.txt", "r")
    alice = libro.read()
    libro.close()

    alice = alice.lower()

    for a in string.punctuation:
        alice = alice.replace(a, " ")

    alice = alice.split()

    diccionario = {}
    for a in alice:
        if a not in diccionario:
            diccionario[a] = 1
        else:
            diccionario[a] += 1

    diccionario_al_reves = {}
    for n in diccionario:
        diccionario_al_reves[diccionario[n]] = n

    las_mas_comunes = {}
    lista_key = sorted(diccionario_al_reves.keys(), reverse=True)

    for n in range(5):
        las_mas_comunes[lista_key[n]] = diccionario_al_reves[lista_key[n]]

    las_mas_comunes_al_reves = {}
    for n in las_mas_comunes:
        las_mas_comunes_al_reves [las_mas_comunes[n]] = n

    print "Las 5 palabras más comunes en ese libro son (palabra:ocurrencia): %s" %las_mas_comunes_al_reves

n_palabras("http://www.gutenberg.org/files/11/11-0.txt")