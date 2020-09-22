from sympy import prod, symbols, Poly, Matrix, pprint, IndexedBase, groebner, simplify
from sympy import LC, LM, LT, reduced, ZZ, degree_list
from sympy.polys.monomials import monomial_deg
from sympy.polys.orderings import monomial_key
from sympy import var, expand, lcm, LM, LT, reduced, monic
from sympy import groebner, solve_poly_system, solve
from sympy.polys.groebnertools import s_poly
from math import sqrt
from sympy.polys.subresultants_qq_zz import *

A, a, b, c, x, y, z, ha, hb, hc, p = symbols('A a b c x y z ha hb hc p')

F = [2*A-a*ha, 2*A-b*hb,2*A-c*hc,
         A**2 - p*(p - a)*(p - b)*(p - c), 2*p - (a + b + c)]

basis = groebner(F, *[a, b, c, p, ha, hb, hc, A], order='lex')
print(len(basis), '\n')
print('triangle', basis, '\n')
area = basis[1]
print('last member of basis = ', area, '\n')

formula = area.subs({p : ((a + b + c) / 2)})
Area = solve(formula, A**2)
Area= simplify(Area)

print("A^2 = ", Area, '\n')
print("A is square root of ", Area, '\n')
#O typos pou prokyptei einai o typos tou Hrwna se ennalaktikh morfh A=\frac{1}{4}\sqrt{2(a^2 b^2+a^2c^2+b^2c^2)-(a^4+b^4+c^4)}


# An theloume na ektypwnei apeytheias to A tote:
# Apo tis opoies 2 rizes kratame thn thetikh giati milame gia emvado
'''Area = solve(formula, A)
Area= simplify(Area)
print("A = ", Area, '\n')
'''
