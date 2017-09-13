#tute sheet 1: least squares

from math import *
from numpy import *
from pylab import *

"data"

U = [91.08, 85.04, 78.54, 68.51, 58.35, 49.63, 41.45, 34.32]
E = [0.8560, 0.8414, 0.8375, 0.8160, 0.7977, 0.7762, 0.7535, 0.7347]

U = array(U)
E = array(E)

"""
Functions set up:
This module is set up so that any data fitting functions,
and any number of them), can be chosen.
"""

def f1(x):
    return x**0
def f2(x):
    return x
def f3(x):
    return x**0.5

f_list = [f1(U), f2(U), f3(U)] 

n = 3 #number of functions

def matrix_construct(U, E, n):
    d = []
    for i in range(n):
        c = []
        for j in range(n):
            c.append(sum(f_list[i]*f_list[j]))
        d.append(c)
        
    d = array(d)
    return d

matrix = matrix_construct(U, E, n)

print(matrix)

def RHS_vector(U,E,n):
    v = []
    for i in range(n):
        v.append(sum(E*f_list[i]))
        
    v = array(v, ndmin=2)
    return v

v = RHS_vector(U,E,n)
v = transpose(v)
print(v)

sol_vector = linalg.solve(matrix,v)
print(sol_vector)

"plot comparison"

L = [sol_vector[i,0] for i in range(len(sol_vector))]

print('L', L)

#L = []
#for i in range(size(solution_vector)):
#    L.append(solution_vector[i,0])

x = array(linspace(min(U), max(U), 20))
f_list2 = [f1(x), f2(x), f3(x)]
m = []
for i in range(n):
    row = []
    row = (L[i]*f_list2[i]).tolist()
    m.append(row)
m = array(m)
#print(m)

y = []
for i in range(len(x)):
    term = 0
    term = sum(m[:,i])
    y.append(term)
    
    
plot(U,E, 'o')
hold = True
plot(x,y)
hold = False
show(block=False)