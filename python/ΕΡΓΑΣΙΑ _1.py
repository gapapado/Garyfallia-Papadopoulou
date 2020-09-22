#######################################################################################################
#     ΟΜΑΔΑ:                           ΑΕΜ:                                                           #
#           ΣΕΤΤΟΣ ΔΗΜΗΤΡΙΟΣ               1324                                                       #    
#           ΜΠΑΜΠΑΛΗΣ ΑΝΑΣΤΑΣΙΟΣ           1407                                                       #
#           ΠΑΠΑΔΟΠΟΥΛΟΥ ΓΑΡΥΦΑΛΛΙΑ        1377                                                       #
#           ΠΟΛΙΤΗΣ ΕΥΑΓΓΕΛΟΣ              1312                                                       #                                                                 #   
#######################################################################################################





"""
This module contains functions for two multivariate resultants. These
are:

- Dixon's resultant.
- Macaulay's resultant.

Multivariate resultants are used to identify whether a multivariate
system has common roots. That is when the resultant is equal to zero.
"""
import pandas as pd
import numpy as np
from sympy import IndexedBase, Matrix, Mul, Poly
from sympy import rem, prod, degree_list, diag
from sympy.core.compatibility import range
from sympy.polys.monomials import monomial_deg, itermonomials
from sympy.polys.orderings import monomial_key
from sympy.polys.polytools import poly_from_expr, total_degree
from sympy.functions.combinatorial.factorials import binomial

from itertools import combinations_with_replacement

# Charalampos Tsiagkalis
from itertools import product
from sympy.core import Mul


def itermonomials_degree_list(variables, max_degrees, min_degrees=None):
    """
    Returns a list of all monomials such that
    min_degrees[i] <= degree_list(monom)[i] <= max_degrees[i]
    for all monom in the list and all i.
    
    If max_degrees = [d_1, ..., d_n] and min_degrees = [e_1, ..., e_n],
    the number of monomials in the list is:

                (d_1 - e_1 + 1) * ... * (d_n - e_n + 1)
    """
    # set min_degrees to zeros when None
    if min_degrees is None:
        min_degrees = [0] * len(max_degrees)

    # check length of arguments
    if (len(variables) != len(max_degrees) or len(variables) != len(min_degrees) ):
        raise ValueError('Argument size does not match')

    # min_degrees[i] <= max_degrees[i] for all i
    if sum([bool(min_degrees[i] <= max_degrees[i])
                    for i in range(len(variables))]) != len(variables):
        raise ValueError('min_degrees[i] must be <= max_degrees[i] for all i.')

    # {x: [min_degree_x, max_degree_x], y: [min_degree_y, max_degree_y], ...}
    variables_dict = {v[0]:list(v[1:]) for v in zip(variables,min_degrees,max_degrees)}

    monomials_list = []
    for variable in variables_dict.keys():
        # monomials of single variables
        current_var_list = []
        for power in range(variables_dict[variable][0], variables_dict[variable][1]+1):
            current_var_list.append(variable**power)
        monomials_list.append(current_var_list)

    return [Mul(*mon) for mon in product(*monomials_list)]

# Serafeim Karaiskos
# Alexandros Bistarakis
def itermonomials_degree_list_K_B( variables, max_degrees, min_degrees = None ):
    """
    Returns a list of all monomials such that
    min_degrees[i] <= degree_list(monom)[i] <= max_degrees[i]
    for all monom in the list and all i.
    
    If max_degrees = [d_1, ..., d_n] and min_degrees = [e_1, ..., e_n],
    the number of monomials in the list is:
    
                (d_1 - e_1 + 1) * ... * (d_n - e_n + 1)
    """
    # set min_degrees to zeros when None
    if min_degrees is None:
        min_degrees = [0]*len(max_degrees)
        
    # check length of arguments
    if (len(variables) != len(max_degrees) or len(variables) != len(min_degrees) ):
        raise ValueError('Argument size does not match')

    # min_degrees[i] <= max_degrees[i] for all i
    if sum([bool(min_degrees[i] <= max_degrees[i])
                    for i in range(len(variables))]) != len(variables):
        raise ValueError('min_degrees[i] must be <= max_degrees[i] for all i.')

    mon1 = [variables[0]**x for x in range(min_degrees[0], max_degrees[0] + 1)]
    # terminating case
    if (len(variables)==1):
        return mon1
    # result
    return [x*y for x in mon1
                    for y in itermonomials_degree_list ( 
                                    variables[1:], 
                                    max_degrees[1:], 
                                    min_degrees[1:])]

# need this extra class for turning tuples into expressions
from sympy.polys.monomials import Monomial

def itermonomials_degree_list_AGA(variables, max_degrees, min_degrees):
    """
    Returns a list of all monomials such that
    min_degrees[i] <= degree_list(monom)[i] <= max_degrees[i]
    for all monom in the list and all i.
    
    If max_degrees = [d_1, ..., d_n] and min_degrees = [e_1, ..., e_n],
    the number of monomials in the list is:
    
                (d_1 - e_1 + 1) * ... * (d_n - e_n + 1)
    """
    # input lists of same length?
    if len(variables) != len(max_degrees) or len(variables) != len(min_degrees):
        raise ValueError('all three input lists should be of same length')
    
    # length of each row to be formed
    columns = len(variables)
    
    # divider of row j while filling a column k.
    div_by = [1]
    
    # min_degrees = [0, ..., 0]?
    if sum(min_degrees) == 0:
        
        # compute the number of rows (monomials)
        rows = 1
        rows = Mul(*[rows * (max_degrees[i] + 1)
                     for i in range(columns)])
            
        # initialize table m having 'rows' rows, where
        # each row is filled with 'columns' zeros.        
        m = [[0 for i in range(columns)] for i in range(rows)]
            
        # copy list max_degrees
        temp = max_degrees[:]

        # update table m
        while sum(temp) != 0:

            # pick k-th column to fill
            k = temp.index(max(temp))
            temp[k] = 0

            # fill in k-th column
            for j in range(rows):
                m[j][k] =  floor(j / Mul(*div_by)) % (max_degrees[k] + 1)

            # update div_by for next column
            div_by.append(max_degrees[k] + 1)
            
    # min_degrees != [0, ..., 0]
    else:
        
        # here diff_degrees in the role of max_degrees 
        diff_degrees = [max_degrees[i] - min_degrees[i]
                        for i in range(columns)]
        
        if any(x < 0 for x in diff_degrees):
            raise ValueError('min_degrees[i] should be <= max_degrees[i] for all i.')
        
        # compute the number of rows (monomials)
        rows = 1
        rows = Mul(*[rows * (diff_degrees[i] + 1)
                     for i in range(columns)])

        # initialize table m having 'rows' rows, where
        # each row is filled with 'columns' zeros.        
        m = [[0 for i in range(columns)] for i in range(rows)]

        # copy the list diff_degrees
        temp = diff_degrees[:]
        
        # update table m
        while sum(temp) != 0:

            # pick k-th column to fill
            k = temp.index(max(temp))
            temp[k] = 0

            # fill in k-th column
            for j in range(rows):
                m[j][k] =  floor(j / Mul(*div_by)) % (diff_degrees[k] + 1)

            # update div_by for next column
            div_by.append(diff_degrees[k] + 1)
        
        # add min_degrees to each row
        m = [[m[j][k] + min_degrees[k] for k in range(columns)]
             for j in range(rows)]
        
    return [Monomial(m[j]).as_expr(*variables) for j in range(rows)]


class DixonResultant():
    """
    A class for retrieving the Dixon's resultant of a multivariate
    system.

    Examples
    ========

    >>> from sympy.core import symbols

    >>> from sympy.polys.multivariate_resultants import DixonResultant
    >>> x, y = symbols('x, y')

    >>> p = x + y
    >>> q = x ** 2 + y ** 3
    >>> h = x ** 2 + y

    >>> dixon = DixonResultant(variables=[x, y], polynomials=[p, q, h])
    >>> poly = dixon.get_dixon_polynomial()
    >>> matrix = dixon.get_dixon_matrix(polynomial=poly)
    >>> matrix
    Matrix([
    [ 0,  0, -1,  0, -1],
    [ 0, -1,  0, -1,  0],
    [-1,  0,  1,  0,  0],
    [ 0, -1,  0,  0,  1],
    [-1,  0,  0,  1,  0]])
    >>> matrix.det()
    0

    See Also
    ========

    Notebook in examples: sympy/example/notebooks.

    References
    ==========

    .. [1] [Kapur1994]_
    .. [2] [Palancz08]_

    """

    def __init__(self, polynomials, variables):
        """
        A class that takes two lists, a list of polynomials and list of
        variables. Returns the Dixon matrix of the multivariate system.

        Parameters
        ----------
        polynomials : list of polynomials
            A  list of m n-degree polynomials
        variables: list
            A list of all n variables
        """
        self.polynomials = polynomials
        self.variables = variables

        self.n = len(self.variables)
        self.m = len(self.polynomials)

        a = IndexedBase("alpha")
        # A list of n alpha variables (the replacing variables)
        self.dummy_variables = [a[i] for i in range(self.n)]

        # A list of the d_max of each variable.
        self.max_degrees = [
            max(degree_list(poly)[i] for poly in self.polynomials)
            for i in range(self.n)]

    def get_dixon_polynomial(self):
        r"""
        Returns
        =======

        dixon_polynomial: polynomial
            Dixon's polynomial is calculated as:

            delta = Delta(A) / ((x_1 - a_1) ... (x_n - a_n)) where,

            A =  |p_1(x_1,... x_n), ..., p_n(x_1,... x_n)|
                 |p_1(a_1,... x_n), ..., p_n(a_1,... x_n)|
                 |...             , ...,              ...|
                 |p_1(a_1,... a_n), ..., p_n(a_1,... a_n)|
        """
        if self.m != (self.n + 1):
            raise ValueError('Method invalid for given combination.')

        # First row
        rows = [self.polynomials]

        temp = list(self.variables)

        for idx in range(self.n):
            temp[idx] = self.dummy_variables[idx]
            substitution = {var: t for var, t in zip(self.variables, temp)}
            rows.append([f.subs(substitution) for f in self.polynomials])

        A = Matrix(rows)

        terms = zip(self.variables, self.dummy_variables)
        product_of_differences = Mul(*[a - b for a, b in terms])
        dixon_polynomial = (A.det() / product_of_differences).factor()

        return poly_from_expr(dixon_polynomial, self.dummy_variables)[0]

    def get_upper_degree(self):
        list_of_products = [self.variables[i] ** self.max_degrees[i]
                            for i in range(self.n)]
        product = prod(list_of_products)
        product = Poly(product).monoms()

        return monomial_deg(*product)

    def get_dixon_matrix(self, polynomial):
        r"""
        Construct the Dixon matrix from the coefficients of polynomial
        \alpha. Each coefficient is viewed as a polynomial of x_1, ...,
        x_n.
        """

        # A list of coefficients (in x_i, ..., x_n terms) of the power
        # products a_1, ..., a_n in Dixon's polynomial.
        coefficients = polynomial.coeffs()
        
        max_degrees = [
            max(degree_list(Poly(poly, self.variables))[i] for poly
                in coefficients) for i in range(self.n)]

        print('max_degrees = ',max_degrees, '\n')
        monomials = list(itermonomials_degree_list(self.variables, max_degrees))

        monomials = sorted(monomials, reverse=True,
                           key=monomial_key('lex', self.variables))
        
        print('monomials - column headers :: ', monomials, '\n')

        dixon_matrix = Matrix([[Poly(c, *self.variables).coeff_monomial(m)
                                for m in monomials]
                                for c in coefficients])

        keep = [column for column in range(dixon_matrix.shape[-1])
                if any([element != 0 for element
                        in dixon_matrix[:, column]])]
        return dixon_matrix[:, keep]



# Example ; Full root recovery; det != 0
print('Example ; Full root recovery; det != 0')
print('\n')

from sympy import symbols, pprint, solve

x, y, z = symbols('x y z')

f = x**2 + y**2 + z**2 - 14
g = x * y + y * z - 33
h = y * z + z**3 - 33

print('f = ', f)
print('g = ', g)
print('h = ', h)
print('\n')

polynomials = [f, g, h]
variables = [x,y]

dixon = DixonResultant(variables=[x, y], polynomials=[f, g, h])
poly = dixon.get_dixon_polynomial()
print('poly = ', poly, '\n')
print('coefficients = ', poly.coeffs(), '\n')

matrix = dixon.get_dixon_matrix(poly)
pprint(matrix)
shape = np.shape(matrix)
final_matrix = np.zeros((shape[0]+1, shape[1]+1))
#final_matrix[,:] = final_matrix[1,:] + matrix[0,:]
print('\n')
print('det = ',matrix.det().factor(), '\n')
print('\n')

a, b = symbols('a b')
List_monomials = [x**1*y**0 , x**0*y**2, x**0*y**1, x**1*y**2 ]
List_index = ['a**2*b**0', 'a**1*b**0', 'a**0*b**1', 'a**0*b**0']

matrix = np.array(matrix)
df = pd.DataFrame(matrix, columns = List_monomials, index = List_index)
df.to_csv('df.csv', index=True, header=True, sep=' ')


print(df)


'''
# The solution of f(x,y,z)=0, g(x,y,z)=0, h(x,y,z)=0 over QQ is:
print('The solution of f(x,y,z)=0, g(x,y,z)=0, h(x,y,z)=0 over QQ is:', '\n')
from sympy import solve_poly_system
print(solve_poly_system([f, g, h], *[x,y,z]))
print('\n')

# The above solution can be found from det = 0 as follows:
print('The above solution can be found from det = 0 as follows:', '\n')

print('the roots of det= 0 are: ', solve((2*z**2 - 1)**4, z))
print('\n')
for value in solve(matrix.det().factor(), z):
    print('for z = ',  value, 'the roots of f(x,y,z)=0, g(x,y,z)=0, h(x,y,z)=0 over QQ are :')
    print('h = ', solve(h.subs(z, value), y))
    print('g = ', solve(g.subs(z, value), x))
    for valueY in solve(h.subs(z, value), y):
        print('y = ',valueY)
        for valueX in solve(g.subs(z, value), x):
            print('x = ',valueX)
            print('f = ', f.subs({x:valueX, y:valueY}))
    print('\n')
'''
