#data_fitting

from numpy import *
from math import *
from pylab import *

"data"
T = arange(0.,200.,20)
mV = [0.01, 0.12, 0.24, 0.38, 0.51, 0.67, 0.84, 1.01, 1.15, 1.3]

assert len(T) == len(mV)

s = 4 # order + 1 of polynomial you'd like to fit

def matrix(T, mV, s):
    mV = array(mV)
    d = []
    for i in range(s):
        c = []
        for j in range(s):
            c.append(sum(mV**(i+j)))
        d.append(c)
        
    d = array(d)
    return d

def rhs_vector(T, mV, s):
    mV = array(mV)
    T = array(T)
    v = []
    for i in range(s):
        v.append(sum(T*(mV**i)))

    v = array(v, ndmin=2)
    return v

Matrix = matrix(T, mV, s)
RHS_v = rhs_vector(T, mV, s)
RHS_v = transpose(RHS_v)

print(Matrix)
print(RHS_v)

solution_vector = linalg.solve(Matrix, RHS_v)
print('solution_vector = ', solution_vector)

"construct line graph"


x = linspace(0, max(mV), 50)
y = []


'''
l = []
for i in range(size(solution_vector)):
    l.append(solution_vector[i,0])
'''

l = [solution_vector[i,0] for i in range(len(solution_vector))]
print(l)
    
for i in range(len(x)):
    term = 0.
    for j in range(len(l)):
        term += l[j]*(x[i])**j
    y.append(term)


figure(1)
plot(mV,T, 'o')
hold = True
plot(x,y)
hold = False
show()


"""
notes:
for order of 10 solution is exact (interpolating function)

"""

    





