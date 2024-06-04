
######################################################
#####            Baby-Step Giant-Step            #####
######################################################

from ECC_tools import fme

def Shanks( G:list , n:int , a:int , b:int ) -> int :
    ''' Algorithme Bay-step Giant-setp '''
    m = sqrt(n)//1 + 1
    hach = {}
    for i in range(m):  #Baby-step
        hach[ fme(a,i,n) ] = i
    alpha = fme(a,n-m,n)
    gamma = b
    for j in range(m):  #Giant-step
        if gamma in hach:
            return i*m+hach[gamma]
        else:
            gamma = (gamma*alpha)%n
    return -1
    
