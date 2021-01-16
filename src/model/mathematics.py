from speechReco import *

def addition(text):
    calcul = text.split(" + ")
    res = 0
    for i in range(len(calcul)):
        res += int(calcul[i])

    print(text + " = " + str(res))

def soustraction(text):
    calcul = text.split(" - ")
    res = 0
    for i in range(len(calcul)):
        res -= int(calcul[i])

    print(text + " = " + str(res))