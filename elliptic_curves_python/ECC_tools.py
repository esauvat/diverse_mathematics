
### Classes point et courbe ###



class Point:
    
    ''' Classe des point de la courbe sauf le point infini '''
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def isInf(self):
        return False

    def co(self):       #Coordonnées du point
        if self.isInf():
            return None
        else:
            return (self.x,self.y)



class PointInf:

    ''' Classe point à l'infini '''
    
    def __init__(self):
        Point.__init__(self,None,None)

    def isInf(self):
        return True

    def co(self):       #Coordonnées du point
        if self.isInf():
            return None
        else:
            return (self.x,self.y)



class Courbe:

    ''' Classe de la courbe '''
    
    def __init__(self,a,b,p):

        ''' Vérification des données '''
        assert a>0
        assert b>0
        assert p>2
        
        self.a = a
        self.b = b
        self.prem = p #Courbe sur Z/pZ

    ''' Fonction vérification d'appartenance '''
    def isOn(self,p):
        if p.isInf():
            return True
        else:
            return ( p.y**2 % self.prem ) == ((p.x**3+self.a*p.x+self.b) %self.prem)

    def egal(self,P,Q):
        if P.isInf():
            return Q.isInf()
        elif Q.isInf():
            return P.isInf()
        else:
            (px,py),(qx,qy) = P.co(),Q.co()
            return px %self.prem==qx %self.prem and py %self.prem==qy %self.prem



def copy(p):
    if p.isInf():
        return PointInf()
    else:
        return Point(p.x,p.y)


    
### Nombre centré ###



def mod(x,p):
    ''' Renvoie le représentant de la classe de x
    dans Z/pZ centré sur 0 '''
    y=x%p
    p2=p//2
    if y<=p2:
        return y
    else:
        return y-p



### Exponentiation modulaire rapide ###



def fme(x,y,n):
    res = 1
    while y>0 :
        if ((y&1)!=0) : 
            res = (res * x) % n
        y= y >> 1
        x = x*x %n
    return mod(res,n)



### Tri fusion pour des couples ###



def fusion_simple(l1,l2):
    res=[]
    i1,i2 = 0,0
    t1,t2 = len(l1),len(l2)
    while i1<t1 and i2<t2:
        if l1[i1]<l2[i2] :
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1
    if i1<t1:
        res = res + l1[i1::]
    else:
        res = res + l2[i2::]
    return res



def ajoute(l,x):
    if l==[] or x[1] != l[-1][1]:
        l.append(x)
    else:
        l[-1] = (fusion_simple(l[-1][0],x[0]),x[1])



def partition(l):
    n=len(l)
    return (l[:n//2],l[n//2::])



def fusion(l1,l2):
    res=[]
    i1,i2 = 0,0
    t1,t2 = len(l1),len(l2)
    while i1<t1 and i2<t2:
        if l1[i1][1]<l2[i2][1] :
            ajoute(res,l1[i1])
            i1 += 1
        else:
            ajoute(res,l2[i2])
            i2 += 1
    while i1<t1:
        ajoute(res,l1[i1])
        i1 += 1
    while i2<t2:
        ajoute(res,l2[i2])
        i2 += 1
    return res



def tri_fus(liste):
    if len(liste) <= 1:
        return liste
    else:
        g,d = partition(liste)
        return fusion(tri_fus(g),tri_fus(d))
    
