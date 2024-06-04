
from ECC_tools import *

### Calcul de l'inverse ###



def inv_mod(x,p):
    if x==0:
        return None
    else:
        return fme(x,p-2,p)



### Somme dans E(K) ###



def somme(P,Q,C):

    ''' Vérification des données '''
    assert C.isOn(P)
    assert C.isOn(Q)

    if P.isInf():   #Cas triviaux
        return Q
    elif Q.isInf():
        return P
    
    else:           #Cas généraux

        n = C.prem
        ((xp,yp),(xq,yq)) = (P.co(),Q.co())
        
        if xp != xq:
            d=inv_mod(xp-xq,n)
            l = mod((yp-yq)*d,n)
            nu = mod((xp*yq-xq*yp)*d,n)
            x1 = mod(l**2-xp-xq,n)
            y1 = mod(-l*x1-nu,n)
            return Point(x1,y1)
        
        elif yp != yq:
            return PointInf()
        
        else:
            
            if yp==0:
                return PointInf()
            
            else:
                d = inv_mod(2*yp,n)
                l = (3*xp**2+C.a)*d
                nu = (-(xp**3)+C.a*xp+2*C.b)*d
                x1 = mod(l**2 - 2*xp,n)
                y1 = mod(-l*x1-nu,n)
                return Point(x1,y1)



### Multiplication dans E(K) ###



def mult(n,P,C):
    
    assert C.isOn(P)

    ''' Calcul de nP dans C par exponentiation rapide '''
    Q = copy(P)
    R = PointInf()
    
    while n>0:
        if ((n&1)==1):
            R = somme(R,Q,C)
        n = n>>1
        Q=somme(Q,Q,C)
    
    return R



### Inverse dans E(K) ###



def inverse(P,C):

    assert C.isOn(P)
    
    (x,y) = P.co()
    return Point(x,-y)
    
