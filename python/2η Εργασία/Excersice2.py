import sympy
from sympy import var, ZZ, sturm, degree
from sympy import intervals, refine_root, N
from sympy import real_roots, CRootOf, Rational, S
from sympy import solve, rootof
from sympy import random_poly, var, Poly, ZZ, S, ceiling, LC
from sympy.polys.subresultants_qq_zz import *


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

def partition(f, LB, UB):
    
    Sseq = sturm(f)
    print("sturm: \n", Sseq)
    
    sL = []
    [sL.append(Sseq[i].subs(x,LB)) for i in range(degree(f,x)+1)]
    print('sL = ', sL, '\n')
    vsL =  variations(sL)
    print('vsL = ', vsL, '\n')

    print("bounds using upperBound LMQ: ", UB,"\n")

    sR = []
    [sR.append(Sseq[i].subs(x,UB)) for i in range(0, degree(f,x)+1)]
    print('sR = ', sR, '\n')
    vsR = variations(sR)
    print('vsR = ', vsR, '\n')

    number_of_roots = vsR-vsL
    
    print("THE NUMBER OF REAL ROOTS BETWEEN", LB ," AND ",UB ," IS: ", abs(number_of_roots))

    return abs(number_of_roots)
    
    

def variations(x):
    counter = 0
    for i in range(len(x)-1):
        if x[i] < 0 and x[i+1] > 0:
            counter = counter + 1
        if x[i] > 0 and x[i+1] < 0:
            counter = counter + 1
    return counter


x = var('x')


#f=random_poly(x,2,-10**2,10**2)
f = x**3 -7*x + 7
lowerbound = 0
upperbound = LMQ(f)

while partition(f, lowerbound, upperbound) > 1:

    middlebound = (lowerbound + upperbound)/2

    left_interval = partition(f, lowerbound, middlebound)
    right_interval = partition(f, middlebound, upperbound)
    
    print("Upperbound: ",upperbound, "middlebound: ", middlebound, "lowerbound: ", lowerbound)
    if right_interval < 1:
        upperbound = middlebound
    if left_interval < 1:
        lowerbound = middlebound
    if left_interval == 1:
        break
    
    
    
        

    
    







    