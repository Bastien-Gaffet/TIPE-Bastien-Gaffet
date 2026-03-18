# from math import *
# import matplotlib.pyplot as plt
#
# from scipy.integrate import odeint
#
# ## Méthode d'Euler pour les équations différentielles d'ordre 1
# ## On travaille dans tout le TD sur l'équadiff
#
# ##    τ y' + y = ...
#
# ## Dans le TD, on fixe la constante de temps τ=1
# ## et on prendra toujours la valeur initiale y0=1
#
# ## Liste des dates
# # nombre de points
# N=20
# ## Q5
# ## Créer la variable tList contenant N points de 0 à 5 inclus, régulièrement espacés
# # Compléter ici même...
# tList = [i*5/(N-1) for i in range(N)]
# #tList = [i//4 for i in range(N)]   [[i for i in range()] for j in range(N)]
# ## Q6
# ## Compléter le code : c'est la fonction F fondamentale de l'équadiff qui calcule
# ## la dérivée y'; ici l'équadiff est homogène.
# def Fequadiff(y,t):
#     return -y
#
# ## Q7
# ## Compléter pour retourner la liste [yk] nommée yList, impérativement de même longueur
# ## que tList (sinon, une erreur surviendra lors du tracé).
# ## (c'est une bonne idée de le vérifier après l'appel, grâce à la commande len).
# # Construit la liste des estimations des yk : fonction sans argumement car la valeur
# # initiale est fixée à 1, et car tList et la fonction de l'équadiff sont des variables
# # globales.
#
# def resoutEuler():
#     yList=[1]
#     for i in range(len(tList)-1):
#         yList.append(yList[i]+Fequadiff(yList[i],tList[i])*(tList[i+1]-tList[i]))
#     return yList
#
# ## Q8
# ## Expliquer les deux premières lignes du code : voir l'aide de odeint
# ## dans le document d'accompagnement.
# def resoutOde():
#     res=odeint(Fequadiff,1,tList) # résoudre l'équation différentielle en retourne un tableau numpy
#     yList=[r[0] for r in res] # exrtrait les valeur du tableau numpy
#     return yList
#
# yList=resoutEuler()
# plt.plot(tList,yList,'b-',label='Euler')
# yList=resoutOde()
# plt.plot(tList,yList,'g-',label='ODE(rk4)')
# ## Q9
# ## Coder la fonction vraie, solution de l'équadiff homogène (compléter)
# def fonctionVraie(t):
#     return exp(-t)
#
# yList=[fonctionVraie(t) for t in tList]
# plt.plot(tList,yList,'r.',label='exact')
# plt.legend()
# plt.show()

## Q10
## Copier le code précédent, du premier yList= jusqu'au plt.show(), et le coller en
## dessous, puis placer le code d'origine en commentaires pour le conserver :
## sélection, clic droit, Commenter
## Modifier le code copié pour afficher les deux fonctions εk, d'Euler, en points
## bleus, et de odeint (Runge-Kutta = RK4), en points rouges.
## Commenter ensuite le code d'Euler pour ne visualiser que les erreurs RK4.

from math import *
import matplotlib.pyplot as plt

from scipy.integrate import odeint

## Méthode d'Euler pour les équations différentielles d'ordre 1
## On travaille dans tout le TD sur l'équadiff

##    τ y' + y = ...

## Dans le TD, on fixe la constante de temps τ=1
## et on prendra toujours la valeur initiale y0=1

## Liste des dates
# nombre de points
N=20
## Q5
## Créer la variable tList contenant N points de 0 à 5 inclus, régulièrement espacés
# Compléter ici même...
tList = [i*5/(N-1) for i in range(N)]
#tList = [i//4 for i in range(N)]   [[i for i in range()] for j in range(N)]
## Q6
## Compléter le code : c'est la fonction F fondamentale de l'équadiff qui calcule
## la dérivée y'; ici l'équadiff est homogène.
def Fequadiff(y,t):
    return -y

## Q7
## Compléter pour retourner la liste [yk] nommée yList, impérativement de même longueur
## que tList (sinon, une erreur surviendra lors du tracé).
## (c'est une bonne idée de le vérifier après l'appel, grâce à la commande len).
# Construit la liste des estimations des yk : fonction sans argumement car la valeur
# initiale est fixée à 1, et car tList et la fonction de l'équadiff sont des variables
# globales.

def resoutEuler():
    yList=[1]
    for i in range(len(tList)-1):
        yList.append(yList[i]+Fequadiff(yList[i],tList[i])*(tList[i+1]-tList[i]))
    return yList

## Q8
## Expliquer les deux premières lignes du code : voir l'aide de odeint
## dans le document d'accompagnement.
def resoutOde():
    res=odeint(Fequadiff,1,tList) # résoudre l'équation différentielle en retourne un tableau numpy
    yList=[r[0] for r in res] # exrtrait les valeur du tableau numpy
    return yList

yList=resoutEuler()
plt.plot(tList,yList,'b-',label='Euler')
yList=resoutOde()
plt.plot(tList,yList,'g-',label='ODE(rk4)')
## Q9
## Coder la fonction vraie, solution de l'équadiff homogène (compléter)
def fonctionVraie(t):
    return exp(-t)

yList=[fonctionVraie(t) for t in tList]
plt.plot(tList,yList,'r.',label='exact')
plt.legend()
plt.show()


## Q11
## Modifier la valeur de N (défini au début du fichier) pour voir son influence sur les
## erreurs commises : N = 1000,  N = 10 (une réexécution du fichier complet par
## "Ctrl-E" doit afficher les nouveaux tracés sans erreurs).

## Q12 : voir doc d'accompagnement
