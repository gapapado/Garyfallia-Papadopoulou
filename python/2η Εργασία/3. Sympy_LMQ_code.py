# -*- coding: utf-8 -*-
"""
Spyder Editor
Upper & Lower bounds on the values of the positive roots
of a polynomial in ZZ[x]
"""
from sympy import random_poly, var, Poly, ZZ, S, ceiling, LC
from sympy import real_roots

x = var('x')


def dup_LC(f, K):
    if not f:
        return K.zero
    else:
        return f[0]
        
def dup_neg(f, K):
    return [ -coeff for coeff in f ]

def dup_root_upper_bound(f, K):
    """
    LMQ as implemented in sympy; corrected by 
    Giannis Parnassos
    """
    n, P = len(f), []
    t = n* [K.one]   #list instead of single counter
    if dup_LC(f, K) < 0:
        f = dup_neg(f, K)
    f = list(reversed(f))

    for i in range(0, n):
        if f[i] >= 0:
            continue

        a, Q = K.log(-f[i], 2), []

        for j in range(i + 1, n):

            if f[j] <= 0:
                continue

            q = t[j] + a - K.log(f[j], 2)
            Q.append([q // (j - i) , j]) #index added to the canditates for minimum

        if not Q:
            continue

        q=min(Q)
        t[q[1]]+=1 #only minimum's t is increased
        P.append(q[0])

    if not P:
        return None
    else:
        return K.get_field()(2)**(max(P) + 1)
    
def LMQ(f):
    """
    Local Max Quadratic
    """
    g= f if LC(f)>0 else -f
    F = list(reversed(Poly(g).all_coeffs()))
    N,temp_max = len(F),0
    if N<=1: return None    
    times_used=[1]*N
    for m in range(N-1,0,-1):
        if F[m-1]<0:
            index=0
            temp_min=S("oo")
            for n in range(N,m,-1):
                if F[n-1]>0:                  
                    q=((2.0**times_used[n-1])*(-F[m-1]/F[n-1]))**(1.0/(n-m))
                    if q<temp_min: 
                        temp_min=q
                        index=n-1
            times_used[index]= times_used[index] +1
#            print times_used
            if temp_max<temp_min: 
                temp_max=temp_min
#    print  temp_max    ,  times_used
    return ceiling((65.0/64)*(temp_max))


i = 0
for i in range(2):
    f=random_poly(x,3,-10**2,10**2)
 #   f=-22*x**17 + 26*x**16 + 70*x**15 + 91*x**14 - 67*x**13 + 80*x**12 + 81*x**11 + 45*x**10 + x**9 - 77*x**8 + 88*x**7 + 52*x**6 + 82*x**5 - 50*x**4 + 4*x**3 + 27*x**2 + 56*x - 17

    print(f)
    print("The real roots of f are located in the intervals:")
    print(real_roots(f))
    print("bounds using sympy functions")
    print(dup_root_upper_bound(Poly(f).all_coeffs(),ZZ))
    # print(dup_root_lower_bound(Poly(f).all_coeffs(),ZZ))
    # print("bounds using giacpy functions")
    # print(gp.posubLMQ(f,x))
    # print(gp.poslbdLMQ(f,x))
    print("bounds using upperBound LMQ")
    print(LMQ(f))
    i = i + 1
