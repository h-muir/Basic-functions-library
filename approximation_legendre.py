from math import *
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt


#Q1: approximating functions with legendre polynomials

def f(x):
    return exp(x)

def P0(x):
    return 1
def P1(x):
    return 2*x-1
def P2(x):
    return 6*(x**2) - 6*x + 1

legendre = {0 : P0,
            1 : P1,
            2 : P2}

n = 3

P_matrix = np.zeros((3,3))
x_vals = np.linspace(0,1,15)
y_vals = np.zeros(len(x_vals))
for i, x in enumerate(x_vals):
    y_vals[i] = f(x)

for i in range(n):
    for j in range(n):
        t_i = 0
        for x in x_vals:
            t_i += legendre[i](x)*legendre[j](x)
        P_matrix[i][j] = t_i

fy = np.zeros(n)
for i in range(n):
    t_i = 0
    for x in x_vals:
        t_i += legendre[i](x)*f(x)
    fy[i] = t_i

inv_P = linalg.inv(P_matrix)
coeffs = np.dot(inv_P, fy)
y_fit = np.linspace(0,0,len(x_vals))

for i,x in enumerate(x_vals):
    y_fit[i] = coeffs[0]*legendre[0](x) + coeffs[1]*legendre[1](x) \
               + coeffs[2]*legendre[2](x)

"""
Compare analytical solutions to numerically calculated coefficients:
a0 = e - 1
a1 = 3(3-e)
a2 = 5(7e-19)
"""

plt.figure()
plt.plot(x_vals, y_vals, 'o')
plt.plot(x_vals, y_fit)
plt.show(block=False)



        

