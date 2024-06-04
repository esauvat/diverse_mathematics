
from ECC_tools import *



def XY_E(C):
    
    p=C.prem  #p premier
    p2=p//2
    
    ''' Création de la liste (y,y^2) '''
    Y = [([0],0)]
    for i in range(1,p2+1):
        Y.append(([-i,i],fme(i,2,p)))
        
    ''' Creation de la liste (x,x^3+ax+b) '''
    X=[]
    for i in range(-p2,p2+1):
        a=(fme(i,3,p)+C.a*i+C.b)%p
        if a>p2:
            a=(a-p)
        X.append(([i],a))
        
    ''' Renvoie des listes triées selon le deuxième élément
    du couple et rassemblée par liste des x dont le second
    élément est identique '''
    return (tri_fus(X),tri_fus(Y))



def ajoute_permut(liste,l1,l2):
    
    a,b = len(l1),len(l2)
    for i in range(a):
        for j in range(b):
            liste.append((l1[i],l2[j]))



def EC(C):
    
    ''' Création de la courbe elliptique '''
    X,Y = XY_E(C)
    supp = [] #Liste des couples (x,y) ATTENTION ce n'est pas la courbe
    ix,iy = 0,0
    tx,ty = len(X),len(Y)
    
    while ix<tx and iy<ty: # Parcours des listes triées linéaire
        if X[ix][1]==Y[iy][1]:
            ''' On ajoute tout les couples (x,y) tels que y^2=x^3+ax+b '''
            ajoute_permut(supp,X[ix][0],Y[iy][0])
            ix += 1
            iy += 1
        elif X[ix][1]<Y[iy][1]:
            ix += 1
        else:
            iy += 1
    
    res = [PointInf()] # Initialisation de la courbe
    #file = open("courbe.txt","w")
    for e in supp:
        res.append(Point(e[0],e[1]))
    #    file.write(str(e) + "\n")
    #file.close()
    return res

def liste(nom):
    lignes = [PointInf()]
    with open(nom,"r",encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.rstrip()
            a,b = tuple(map(int, ligne[1:-1].split(',')))
            lignes.append(Point(a,b))
        return lignes
