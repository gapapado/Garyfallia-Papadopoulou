from sympy import IndexedBase, Matrix, Mul, Poly, floor, var, pprint, S
from sympy import rem, prod, degree_list, total_degree, apart, residue, series, together
from sympy import numbered_symbols, take, fps, collect, groebner, Rational
from sympy import sqf, sqf_list, quo, diff, integrate, sqrt, cos, Integral, together, cot, sin
from sympy import numer, denom, gcd, degree
from sympy.series.formal import compute_fps
from sympy.core.compatibility import range
from sympy.polys.monomials import monomial_deg
from sympy.polys.monomials import itermonomials
from sympy.polys.orderings import monomial_key
from sympy.polys.polytools import *
from sympy.functions.combinatorial.factorials import binomial
from sympy.functions.combinatorial.factorials import *
from sympy import *
from sympy.functions.combinatorial.numbers import *
from itertools import combinations_with_replacement, combinations, product
from sympy import symbols, solve, factor, expand, simplify, nsimplify, solve_undetermined_coeffs
from fractions import Fraction
import numpy as np
from sympy import LM
from sympy.abc import x
from sympy import summation , oo , symbols, log




k = 5
print([stirling(k, i, kind=2) for i in range(1, k+1)])

i, a, b, x = symbols('i, a, b, x')

p = x**7 - (S(7)/9)*x**5 + S(7)/13

print(p.args)
dunameis = p.args
dunameis = np.array(dunameis)

k = np.zeros(len(dunameis))
StirList = np.zeros((len(dunameis)))
k = k.astype(int)
Lista = list()

for i in range (0,len(dunameis)):
    k[i] = degree(dunameis[i])
    StirList = ([stirling(k[i], n, kind=2) for n in range(0, k[i]+1)])
    poly1 = np.poly1d(StirList[::-1])
    Lista.append(poly1)

p1 =0 
for i in range (0, len(Lista)):
    p1 = p1 + Lista[i]
print(p1)
# orizoume to polywnymo pou proekypse
p2= x**7 + 21*x**6 + 141*x**5 + 360*x**4 + 326*x**3 + 78*x**2 + 2*x + 1
''''
result = integrate(p2, (x,a,b))
print('result = ', result)
filiw = (ff(b,8) - ff(a, 8) ) / 8

f = - (ff(b,8) - ff(a,8)) / 8 - 3 * (ff(b,7) - ff(a,7)) - (47/2) * (ff(b,6) - ff(a,6)) + 360 * (ff(b,5) - ff(a,5)) / 5 + 326 * (ff(b,4) - ff(a,4)) / 4 + 78 * (ff(b,3) - ff(a,3)) / 3 + 2 * (ff(b,2) - ff(a,2)) / 2
    

print(expand(filiw))
print('\n')
print(expand(f))


result = integrate(p2, (x,a,b))
print(result)
f = (ff(b+1,8) - ff(a,8)) / 8 + 3 * (ff(b+1,7) - ff(a,7)) + (47/2) * (ff(b+1,6) - ff(a,6)) + 72 * (ff(b+1,5) - ff(a,5)) + (163/2) * (ff(b+1,4) - ff(a,4)) + 26 * (ff(b+1,3) - ff(a,3)) + (ff(b+1,2) - ff(a,2))
print('\n')
print(expand(f))


man= summation(x**7 + 21*x**6 + 141*x**5 + 360*x**4 + 326*x**3 + 78*x**2 + 2*x + 1, (x, a, b))
print('\n', man)     

'''



'''
print(LM(p2))
sum1 = 0
temp = 0 
for i in range (0, degree(p2)):

    term = LM(p2)
    #sum1 = sum1 + ff(b + 1, degree(term) + 1) - ff(b, degree(term) + 1)
    
  
    sum1 = sum1 * LC(p2)
    p2 = p2 - LT(p2)
    print(p2)
print(expand(sum1))
'''