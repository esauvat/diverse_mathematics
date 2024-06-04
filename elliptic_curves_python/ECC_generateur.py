
from ECC_tools import *
from ECC_courbe import *
from ECC_calcul import *



def diviseurs(n:int) -> list:
    res = []
    for i in range(1,n+1):
        if n==(n//i)*i:
            res.append(i)
    return res

def ordre(P,Q,liste_d,C):
    if Q.isInf():
        for e in liste_d:
            if mult(e,P,C).isInf():
                return e
    else:
        for e in liste_d:
            if C.egal(mult(e,P,C),Q):
                return e
        return -1

def generateur(E,C):
    p=len(E)
    R=PointInf()
    j=1
    liste_d = diviseurs(p)
    x=liste_d[len(liste_d)//2]
    for P in E:
        o = ordre(P,R,liste_d,C)*j
        if o==p:
            return P
        elif o>x:
            R=P
            j=o
            liste_d=diviseurs(o)
            x=liste_d[len(liste_d)//2]

            
def generateur2(E,C):
    p=len(E)
    liste_d = diviseurs(p)[:-1]
    for P in E:
        flag = True
        for e in liste_d:
            if mult(e,P,C).isInf():
                flag = False[
                break
        if flag:
            return P

def generateur3(E,C):
    p=len(E)
    liste_d = diviseurs(p)[:-1]
    dic = {}
    dic[PointInf()]=0
    for P in E:
        if not(P in dic):
            flag = True
            for e in liste_d:
                if mult(e,P,C).isInf():
                    flag = False
                    Q=copy(P)
                    for i in range(e-1):
                        dic[Q]=0
                        Q=somme(P,Q,C)
            if flag:
                return P
    return PointInf()
                
