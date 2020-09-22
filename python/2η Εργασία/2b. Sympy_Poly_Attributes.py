from sympy import var, solve, rootof, RootOf, CRootOf

from sympy.polys.subresultants_qq_zz import *

x = var('x')

###############
f = x**3 - 7*x + 7
g = f * (x - 3)
###############
print('derivative of f is : ', f.as_poly().diff())
print('integral of f is : ', f.as_poly().integrate())
print('gcd(f, diff(f)) is : ', f.as_poly().gcd(f.as_poly().diff()))
print('gcd(f, g) is : ', f.as_poly().gcd(g.as_poly()))
print('real root isolating intervals of f are : ',
      f.as_poly().intervals(),'\n')
print('sturm sequence of f is = ', f.as_poly().sturm())
print('real roots of f are = ', f.as_poly().real_roots())
###############
f1 = x**2 + 4
pprint(f1)
###############
print('complex roots of f1 are = ', solve((f1), x))
print('complex roots of f1 are = ', rootof((f1), x, 0))
print('complex roots of f1 are = ', CRootOf((f1), x, 0))
print('complex roots of f1 are = ', RootOf((f1), x, 0))

f2 = x**2 +1

print('*****complex roots of f2 are = ', CRootOf((f2), x, 1))
print('complex roots of f1 are = ', solve((f2), x))
print('roots of f1 are = ', rootof((f2), x, 0))
print('complex roots of f1 are = ', RootOf((f2), x, 1))