#Robust Newton's method

from math import *
from numpy import *

def f1(x,y):
    return (x**2+y**2)**2 - 18*(x**2-y**2)

def f2(x,y):
    return 183 - 128*x + 20*x**2 + 26*y - 12*x*y + 8*y**2

def Jm(f1, f2, x, y, h):
    J = zeros((2,2))
    J[0,0] = (f1(x+h,y) - f1(x,y))/h
    J[0,1] = (f1(x,y+h) - f1(x,y))/h
    J[1,0] = (f2(x+h,y) - f2(x,y))/h
    J[1,1] = (f2(x,y+h) - f2(x,y))/h
    return J

def C(a,b):
    return linalg.solve(a,b)

n = 10
h = 0.1

P = array([2.0, 1.0])

for i in range(n):
    print('i:', i)
    F = array([f1(P[0], P[1]), f2(P[0], P[1])])
    J = Jm(f1, f2, P[0], P[1], h)
    for d in range(50):
        LHS = linalg.norm(array([f1(P[0]-(1/2**d)*C(J,F)[0], P[1]-(1/2**d)*C(J,F)[1]),
                          f2(P[0]-(1/2**d)*C(J,F)[0], P[1]-(1/2**d)*C(J,F)[1])]))
        RHS = (1-1/2**(d+2))*linalg.norm(F)
        print(LHS, RHS)
        if LHS < RHS:
            D = d
            print('D=', D)
            break
        else:
            D = 0
    P = P-(1/2**D)*C(J,F)
    print('current P', P)


    
