from sympy import Abs, var, rem
from sympy import prem, degree

from sympy.polys.subresultants_qq_zz import *

x = var('x')


def our_gcd(a, b):
    """
    Μέγιστος κοινός διαιρέτης ακεραίων
    """
    counter = 0   # για τον αριθμό των διαιρέσεων
    while b:
        a, b = b, a%b
        counter = counter + 1  
    print('counter = ', counter,'\n')
    return Abs(a)

print('Μέγιστος κοινός διαιρέτης ακεραίων','\n')
    
print( 'gcd = ', our_gcd(21, 8),'\n','\n')

print('Μέγιστος κοινός διαιρέτης πολυωνύμων')

print("\n\nExample 10  incomplete. \n")
print( "degree difference 2\n")
f = x**8 + x** 6 - 3*x** 4 - 3*x** 3 + 8*x **2 + 2*x - 5
g = 3*x** 6 + 5*x** 4 - 4*x** 2 - 9*x + 21

print('f = ', f,'\n')
print('g = ', g,'\n')

print('Περίπτωση Α:','\n')

print('Οι παραστάσεις f, g θεωρούνται πολυώνυμα όπότε έχουν')
print('την ιδιότητα (attribute) gcd:  f.as_poly().gcd(g.as_poly())', '\n')

print('gcd(f, g) = ', f.as_poly().gcd(g.as_poly()),'\n')


print('Περίπτωση B:','\n')
    
print('Τα f, g θεωρούνται παραστάσεις','\n')
      
def our_euclid_rem(f, g, x):
    """
    Μέγιστος κοινός διαιρέτης πολυωνύμων
    f and g, deg(f) > deg(g) > 0 στους ρητούς (QQ).
    Τα υπόλοιπα κάθε διαίρεσης υπολογίζονται με την
    συνάρτηση rem(). Τα πρόσημα των υπολοίπων είναι σωστά.
    """
    print('gcd(f, g) using rem()','\n')
    print(f, '\n')
    print(g, '\n')
    our_es = [f, g]
    while degree(g, x) > 0:
        h = rem(f, g)
        our_es.append(h)
        f, g = g, h
        print(g, '\n')
    return our_es

es = our_euclid_rem(f, g, x)
print( sign_seq(es, x) , '\n')


def our_euclid_prem(f, g, x):
    """
    Μέγιστος κοινός διαιρέτης πολυωνύμων
    f and g, deg(f) > deg(g) > 0 στους ακεραίους (ZZ).
    Τα υπόλοιπα κάθε διαίρεσης υπολογίζονται με την
    συνάρτηση prem(). Τα πρόσημα των υπολοίπων ΔΕΝ είναι
    πάντα σωστά.
    """
    print('gcd(f, g) using prem()','\n')
    print(f, '\n')
    print(g, '\n')
    our_es = [f, g]
    while degree(g, x) > 0:
        h = prem(f, g)
        our_es.append(h)
        f, g = g, h
        print(g, '\n')
    return our_es

es = our_euclid_prem(f, g, x)
print( sign_seq(es, x) , '\n')


def our_euclid_rem_z(f, g, x):
    """
    Μέγιστος κοινός διαιρέτης πολυωνύμων
    f and g, deg(f) > deg(g) > 0 στους ακεραίους (ZZ).
    Τα υπόλοιπα κάθε διαίρεσης υπολογίζονται με την
    συνάρτηση rem_z(). Τα πρόσημα των υπολοίπων είναι σωστά.
    """
    print('gcd(f, g) using rem_z()','\n')
    print(f, '\n')
    print(g, '\n')
    our_es = [f, g]
    while degree(g, x) > 0:
        h = rem_z(f, g, x)
        our_es.append(h)
        f, g = g, h
        print(g, '\n')
    return our_es

es = our_euclid_rem_z(f, g, x)
print( sign_seq(es, x) , '\n')




