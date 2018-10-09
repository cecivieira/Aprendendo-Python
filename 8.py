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

    print diccionario
    libro.close()

n_palabras("http://www.gutenberg.org/files/11/11-0.txt")

#