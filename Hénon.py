import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
 
"""------Variable------"""
 
# paramètres
a = 0
b = 0
n = 1
# premier de la suite X(n)
X_0 = 0
Y_0 = 0
 
"""----Fonctions-----"""
 
 
def verifpara(bol, para):
    if (para == "a"):
        if (bol == False):
            print("erreur de saisie, veuillez respecter les conditions d'entrée")
        try:
            a = float(input('entrez le paramètre a ( 1 <= a <= 1.5)'))
            if (1 <= a) and (a <= 1.5):
                return (a)
        except ValueError:
            veriffloat(False, "a",)
    elif (para == "b"):
        if (bol == False):
            print("erreur de saisie, veuillez respecter les conditions d'entrée")
        try:
            b = float(input("entrez le paramètre b ( 0 <= b <= 0.4 )"))
            if (0 <= b) and (b <= 0.4):
                return (b)
        except ValueError:
            veriffloat(False, "b",)
    elif (para == 'x'):
        if (bol == False):
            print("erreur de saisie, veuillez respecter les conditions d'entrée")
        try:
            return float(input('entrez X zéro'))
        except ValueError:
            veriffloat(False, "x",)
    elif (para == 'y'):
        if (bol == False):
            print("erreur de saisie, veuillez respecter les conditions d'entrée")
        try:
            return float(input("entrez y zéro"))
        except ValueError:
            veriffloat(False, "y",)
    elif (para == "n"):
        if (bol == False):
            print("erreur de saisie, veuillez respecter les conditions d'entrée")
        try:
            n = int(input('entrez nombre de point'))
            if (n > 0):
                return (n)
        except ValueError:
            veriffloat(False, "n",)
 
 
def suiteY(xo, yo, a, b, k,):  # ( X_0, Y_0, A, B, n,)
    ty = np.arange(k, dtype=float)
    tx = np.arange(k, dtype=float)
    tx[0] = xo
    ty[0] = yo
    i = 0
    while (i < k - 1):
        ty[i + 1] = b * tx[i]
        tx[i + 1] = 1 + ty[i] - a * tx[i] * tx[i]
        i = i + 1
 
    return(ty)
 
 
def suiteX(xo, yo, a, b, k,):  # ( X_0, Y_0, A, B, n,)
    ty = np.arange(k, dtype=float)
    tx = np.arange(k, dtype=float)
    tx[0] = xo
    ty[0] = yo
    i = 0
    while (i < k - 1):
        ty[i + 1] = b * tx[i]
        tx[i + 1] = 1 + ty[i] - a * tx[i] * tx[i]
        i = i + 1
 
    return(tx)
 
 
"""----Programme----"""
"""
X_0 = verifpara(True, 'x',)
print(X_0)
Y_0 = verifpara(True, 'y',)
print(Y_0)
a = verifpara(True, "a",)
print(a)
b = verifpara(True, "b",)
print(b)
n = verifpara(True, "n",)
print(n)

plt.scatter(suiteX(X_0, Y_0, a, b, n), suiteY(X_0, Y_0, a, b, n))
plt.show()


plt.scatter(suiteX(1, 1, 1.4, 0.3, 100000), suiteY(1, 1, 1.4, 0.3, 100000))
"""



"""Actracteur no zoomé"""
ax = plt.subplot(111)
ax.scatter(suiteX(1, 1, 1.4, 0.3, 100000), suiteY(1, 1, 1.4, 0.3, 100000),0.5)


""" 1ère fenêtre de zoom"""
ax2 = plt.axes([.2, 0.6, .3, .3])
ax2.scatter(suiteX(1, 1, 1.4, 0.3, 10000000), suiteY(1, 1, 1.4, 0.3, 10000000),0.01)
ax2.axis([0.302,0.312,0.205,0.215])
rect1 = patches.Rectangle((0.302,0.205),0.01,0.01,linewidth=1,edgecolor='r',facecolor='none')
ax.add_patch(rect1)
plt.yticks(visible=False)
plt.xticks(visible=False)

""" 2nde fenêtre de zoom"""
ax3 = plt.axes([.6, 0.6, .3, .3])
ax3.scatter(suiteX(1, 1, 1.4, 0.3, 10000000), suiteY(1, 1, 1.4, 0.3, 10000000),0.01)
ax3.axis([0.305,0.3055,0.2105,0.211])
rect2 = patches.Rectangle((0.305,0.2105),0.0005,0.0005,linewidth=1,edgecolor='g',facecolor='none')
ax.add_patch(rect2)
plt.yticks(visible=False)
plt.xticks(visible=False)


plt.show()
