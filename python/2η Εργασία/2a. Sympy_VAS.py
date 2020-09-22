from sympy import var, ZZ
from sympy import intervals, refine_root, N
from sympy import real_roots, CRootOf, Rational, S


from sympy.polys.rootisolation import *

from sympy.polys.subresultants_qq_zz import *

x = var('x')

f = x**3 - 7*x + 7
print('f as an arithmetic expression:', f,  '\n')

print('using the private function dup_...  = ',
      dup_isolate_real_roots( f.as_poly().all_coeffs(), ZZ), '\n')

intrvs = intervals(f)

print('using the @public function intervals = ', intrvs, '\n')

print('last root refined with Rational = ',
      refine_root(x**3-7*x+7,Rational(2,1),Rational(3,2), eps=1e-16), '\n')

print('last root refined with S = ',
      refine_root(x**3-7*x+7,S(3)/2,S(2)/1, eps=1e-16), '\n')

roots = []
for i in range(len(intrvs)):
    a = intrvs[i][0]
    b = a[0]
    c = a[1]
    d = refine_root(f, b, c, eps=1e-25)
    roots.append(N(d[0],25))
print('ALL roots refined = ', roots, '\n')

print('ANOTHER way to handle roots with the public function real_roots() :',
      real_roots(f), '\n')

print('Evaluate them WHEN you need them (lazy evaluation) :',
      N( CRootOf(x**3 - 7*x + 7, 1), 50), '\n')

print('f as a Polynomial ... : ', f.as_poly(), '\n')

print('... has the attribute real_roots(); i.e. f.as_poly().real_roots() : ',
      f.as_poly().real_roots(), '\n')




