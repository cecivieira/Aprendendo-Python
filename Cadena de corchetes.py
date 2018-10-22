#coding=utf-8
# 7. Escribe una función que Determine si una cadena formada por corchetes es equilibrada, es decir, si consiste
# enteramente de pares de apertura / cierre de corchetes (en ese orden), y todos los corchetes abiertos se cierran
# correctamente.
#   []        OK   ][        NOT OK
#   [][]      OK   ][][      NOT OK
#   [[][]]    OK   []][[]    NOT OK

def corchetes(x):
    x = list(x)
    fim = len(x)-1
    inicio = 0

    while inicio != fim:
        if x[inicio] == "[":
            meio = inicio + 1
            while meio <= fim:
                if x[meio] == "]":
                    x[meio] = "v"
                    x[inicio] = "v"
                    break

                elif meio == fim:
                    inicio += 1
                    break

                elif meio < fim:
                    meio += 1

        else:
            inicio += 1

    if "[" in x or "]" in x:
        print "La cadena formada por corchetes NO es equilibrada "

    else:
        print "La cadena formada por corchetes es equilibrada "

corchetes("[]][[[[[]")
