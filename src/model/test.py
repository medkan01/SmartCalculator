from speechReco import *

t1 = ""

t2 = t1.split(" ")

print(t2)
#Il faut donner la priorité aux multiplications et aux divisions --> utiliser la fonction python qui vérifie si un caractère est dans une liste ou pas.
try:
    res = 0
    if(t2[0].isnumeric()):
        res = int(t2[0])
    for i in range(len(t2)):
        if(t2[i] == "-"):
            res -= int(t2[i+1])
            print(str(i) + ". [DEBUG] res = " + str(res))
        elif(t2[i] == "+"):
            res += int(t2[i+1])
            print(str(i) + ". [DEBUG] res = " + str(res))
        elif(t2[i] == "x"):
            res *= int(t2[i+1])
            print(str(i) + ". [DEBUG] res = " + str(res))
        elif(t2[i] == "/"):
            res /= int(t2[i+1])
            print(str(i) + ". [DEBUG] res = " + str(res))
except Exception as e:
    print("Attention! Il y a une erreur dans le calcul demandé, veuillez vérifier puis rééssayer")