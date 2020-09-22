
# coding: utf-8

# In[14]:


#Αλέξανδρος Κόντος 1526, Σπύρος Βασιλείου 1522, Παναγιώτης Κλωνής 1309, Αντώνης Μάτζος 1293

#PART A

from sympy import var, expand, lcm, LM, LT, reduced, monic
from sympy import groebner, solve_poly_system, solve
from sympy.polys.groebnertools import s_poly

#pairnoume tis eksiswseis [A**2 - p*(p - a)*(p - b)*(p - c)] kai [2*p - (a + b + c)]
A, a, b, c, p, x = var('A, a, b, c, p, x')
F = [A**2 - p*(p - a)*(p - b)*(p - c), 2*p - (a + b + c)]

basis = groebner(F, *[p, a, b, c, A], order='lex')
print(len(basis), '\n')
print(basis), '\n
print('triangle', basis, '\n')
area = basis[1]
print('last member of basis = ', area, '\n')
formula = area.subs({A**2 : x})
print('poly in x**2 :: ', formula, '\n')
print('Area of the triangle :: ', expand( solve(formula, x)[0]))


# In[18]:


#PART B
#prosthetoume tis eksiswseis ma=sqrt((2*b**2+2*c**2-a**2)/4), mb=sqrt((2*a**2+2*c**2-b**2)/4), mc=sqrt((2*a**2+2*b**2-c**2)/4)
#kai tis vazoume na einai ises me to 0, diladi tis pame oles apo tin aristeri meria
A, a, b, c, p, x, ma, mb, mc = var('A, a, b, c, p, x, ma, mb, mc')
F = [A**2 - p*(p - a)*(p - b)*(p - c), 2*p - (a + b + c),
     4*ma**2 - 2*b**2 - 2*c**2 + a**2, 4*mb**2 - 2*a**2 - 2*c**2 + b**2, 4*mc**2 - 2*a**2 - 2*b**2 + c**2]

basis = groebner(F, *[a, b, c, p, ma, mb, mc, A], order='grlex')
print(len(basis), '\n')
print('triangle', basis, '\n')
area = basis[0]
print('last member of basis = ', area, '\n')
formula = area.subs({A**2 : x})
print('poly in x**2 :: ', formula, '\n')
#i riza pou pairnoume einai dipli eite valoume 1 h 0 mesa stin solve
print('Area of the triangle :: ', expand( solve(formula, x)[1]))

