#######################################################################################################
#     ΟΜΑΔΑ:                           ΑΕΜ:                                                           #
#           ΣΕΤΤΟΣ ΔΗΜΗΤΡΙΟΣ               1324                                                       #    
#           ΜΠΑΜΠΑΛΗΣ ΑΝΑΣΤΑΣΙΟΣ           1407                                                       #
#           ΠΑΠΑΔΟΠΟΥΛΟΥ ΓΑΡΥΦΑΛΛΙΑ        1377                                                       #
#           ΠΟΛΙΤΗΣ ΕΥΑΓΓΕΛΟΣ              1312                                                       #                                                                 #   
#######################################################################################################







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
from sympy.abc import x, a, b 

i, a, b, x = symbols('i, a, b, x')

p = x**7 - (S(7)/9)*x**5 + S(7)/13

##
## Ο πίνακας "orismata" περιλαμβάνει τον κάθε όρο του πολυωνύμου που πρόκειται να επεξεργαστούμε
##

orismata = p.args
orismata = np.array(orismata)
print('Mononuma tou poluonumou:',orismata,'\n')
p = Poly(p, x)
          
s = p.coeffs()                                     ###### Πίνακας συντελεστών πολυωνύμου
s = np.array(s)
print('Οι συντελεστές του αρχικού πολυωνύμου:', s)
k = np.zeros(len(orismata))                        ###### Πίνακας δυνάμεων πολυωνύμου
StirList = np.zeros((len(orismata)))
k = k.astype(int)
Lista = list()

for i in range (0,len(orismata)):
    if degree(orismata[i]) == 0:
        k[i] = 0
    k[i] = degree(orismata[i])
    
k.sort(axis=-1, kind='quicksort', order=None)
k = k[::-1]
print('\nΟι βαθμοί των μονωνύμων είναι:',k,'\n')

print('Οι αριθμοί Stirling είναι:')
for i in range (0,len(orismata)):

    StirList = ([stirling(k[i], n, kind=2) for n in range(0, k[i]+1)])
    print(StirList,'\n')
    poly1 = np.poly1d(StirList[::-1])*s[i]
    Lista.append(poly1)
    
p1 = 0
for i in range (0, len(Lista)):
    p1 = p1 + Lista[i]
    
print('\nΗ συνάρτηση που προκύπτει είναι:\n',p1,'\n')

p1 = Poly(p1, x)
result= integrate(p1, (x,0,x))


syntelestes=result.coeffs()
syntelestes = syntelestes[::-1]
Lista2=list()

for i in range (0 , 8)  :
    temp = syntelestes[i]*((ff(b+1,i+1)) -  ff(a,i+1))
    Lista2.append(temp)
    
    
p3 = 0 
for i in range (0, len(Lista2)):
    p3 = p3 + Lista2[i]
print('\n''\n')


p3 = Poly(p3, a, b)
print('\n',p3)



c= p3.coeffs()
c = np.array(c)
for i in range(0, len(c)):
    c[i] = Rational(c[i]).limit_denominator()

##
#  Εκτυπώνουμε ξανά τους συντελεστές στη σωστή μορφή όπως θα έδινε η summation
#   και παραθέτουμε και την επαλήθευσή της
##    
print('\n',c)    
print('\n',simplify(summation(p, (x, a, b))))
