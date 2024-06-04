
import matplotlib.pyplot as plt
from ECC_tools import *
from ECC_courbe import *



def illustr(C):
    
    E = EC(C)
    E1 = [e.x for e in E[1::]] #Liste des abscisses
    E2 = [e.y for e in E[1::]] #Liste des ordonnées

    ''' Création du graphe '''
    premier = "p="+str(C.prem) 
    plt.title(premier)
    
    p2=C.prem//2
    a=2
    plt.axis([-a*p2,a*p2,-a*p2,a*p2])

    plt.clf()
    plt.plot(E1,E2,'.',markersize=2, color='#ffb859',
             label='Courbe (a=' + str(C.a) + ',b=' +str(C.b) +')')
    plt.grid()
    plt.legend()
    plt.show()
