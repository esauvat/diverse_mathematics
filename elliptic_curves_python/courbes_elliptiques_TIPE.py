def classe(a,p):
    return a%p

def points(C,p):
    L=[]
    for i in range(p):
        L.append((i,classe(i**3+C[0]*i+C[1],p)))
    D={}
    for i in range(p):
        D[i]=classe(i*i,p)
    F=[]
    for i in range(len(L)):
        for k in D:
            if L[i][1]==D[k]:
                F.append((L[i][0],k))
    return F
        
def verification(P,C,p):
    if classe(P[0]**3+C[0]*P[0]+C[1],p)==classe(P[1]**2,p):
        return True
    return False
    
def loi_ct(P,Q,C,p):
    if not verification(P,C,p) or not verification(Q,C,p):
        return "compliqué sans des points appartenant à la courbe"
    O=(0,1)
    if P==O and Q==O:
        return O
    elif P==O:
        return (Q[0],-Q[1])
    elif Q==O:
        return (P[0],-P[1])
    elif P[0]==Q[0]:
        if P[1]==Q[1]:
            if P[1]==0:
                return O
            x=(3*P[0]**2+C[0])/(2*P[1])
            y=(-P[0]**3+C[0]*P[0]+2*C[1])/(2*P[1])
            return (x**2-2*P[0],x(x**2-2*P[0])+y)
        return O
    x=(P[1]-Q[1])/(P[0]-Q[0])
    y=(P[0]*Q[1]-Q[0]*P[1])/(P[0]-Q[0])
    return (x**2-P[0]-Q[0],x*(x**2-P[0]-Q[0])+y)


