#######################################################################################################
#     ΟΜΑΔΑ:                           ΑΕΜ:                                                           #
#           ΜΑΚΡΗΣ ΔΗΜΗΤΡΙΟΣ               514                                                        #    
#           ΜΠΑΜΠΑΛΗΣ ΑΝΑΣΤΑΣΙΟΣ           1407                                                       #
#           ΠΑΠΑΔΟΠΟΥΛΟΥ ΓΑΡΥΦΑΛΛΙΑ        1377                                                       #
#           ΠΟΛΙΤΗΣ ΕΥΑΓΓΕΛΟΣ              1312                                                       #
#           ΤΖΟΥΝΑΣ ΣΤΕΦΑΝΟΣ               1391                                                       #   
#######################################################################################################




from sympy import (var, degree, diff, Poly, expand, sturm,
                   Matrix, pprint, rem, det)
from sympy.polys.subresultants_qq_zz import *
from sympy import random_poly


x = var('x')
Sseq = []


n = input("Give degree of polynomial f: ")
n = int(n)
w = input("Give degree of polynomial g: ")
w = int(w)

#######################################################################################################

##########    ΕΑΝ ΘΕΛΟΥΜΕ Η "g" ΣΥΝΑΡΤΗΣΗ ΝΑ ΕΙΝΑΙ ΠΑΡΑΓΩΓΟΣ ΤΗΣ "f" ΜΠΟΡΟΥΜΕ ΝΑ ΧΡΗΣΙΜΟΠΟΙΗΣΟΥΜΕ ΤΟΝ
##########    ΠΑΡΑΚΑΤΩ ΚΩΔΙΚΑ ΧΩΡΙΣ ΝΑ ΖΗΤΑΜΕ ΤΟΝ ΒΑΘΜΟ ΤΗΣ "g" ΓΙΑ ΤΗ ΔΗΜΙΟΥΡΓΙΑ Random ΣΥΝΑΡΤΗΣΗΣ:
#
#             f=random_poly(x, n, -10**2, 10**2)
#             g = diff(f, x, 1)
#
#######################################################################################################



f=random_poly(x, n, -10**2, 10**2)
g = random_poly(x, w, -10**2, 10**2)
if degree(g) > degree(f):
    temp = f
    f = g
    g = temp
deg_r = degree(g) - 1

Sseq.append(f)
Sseq.append(g)

print('sylvester 2','\n')
m = sylvester(f, g, x, 2)
pprint(m)
print('\n')
c = det(m)

deleted_rows = 2 * deg_r
num_of_rows = (degree(f) * 2) - deleted_rows

m2 = m[0:num_of_rows,:]
pprint(m2)
print('\n')

List = []
i = 0
while i < degree(g):
    coeff = det(m2[:,0:num_of_rows])
    List.append(coeff)
    j = num_of_rows + i
    m2.col_swap(num_of_rows-1, j)
    pprint(m2)
    print('\n')
    i = i + 1
    
print(List)
r = 0
for i in range (len(List)):
    
    r += List[i]*x**(deg_r-i)
        
Sseq.append(r)
Sseq.append(c)
print('\nSturm Sequence is: ', Sseq)




