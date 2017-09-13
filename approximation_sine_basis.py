from math import *
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt


#Q3

#function
def f(x):
    return x*(pi-x)

#basis functions
def P0(x):
    return sin(x)
def P1(x):
    return sin(2*x)
def P2(x):
    return sin(3*x)

#function dictionary
P_basis = { 0 : P0,
            1 : P1,
            2 : P2 }

n = 3 #number of basis functions

P_matrix = np.zeros((3,3)) #initialise matrix
x_vals = np.linspace(0,pi,30) #NOTE: domain important for basis functions 
y_vals = np.zeros(len(x_vals))
for i, x in enumerate(x_vals):
    y_vals[i] = f(x)

#construct matrix
for i in range(n):
    for j in range(n):
        t_i = 0
        for x in x_vals:
            t_i += P_basis[i](x)*P_basis[j](x)
        P_matrix[i][j] = t_i

#RHS vector
fy = np.zeros(n)
for i in range(n):
    t_i = 0
    for x in x_vals:
        t_i += P_basis[i](x)*f(x)
    fy[i] = t_i

#solve for coefficients
inv_P = linalg.inv(P_matrix)
coeffs = np.dot(inv_P, fy)
y_fit = np.linspace(0,0,len(x_vals))

#plot approximated function
for i,x in enumerate(x_vals):
    y_fit[i] = coeffs[0]*P_basis[0](x) + coeffs[1]*P_basis[1](x) \
               + coeffs[2]*P_basis[2](x)

print(coeffs)
"""
observe that the second coefficient = 0
means that the sin(2x) basis function is omitted
approximating function = 2.5465*sin(x) + 0.0943*sin(3x)
"""

plt.figure()
plt.plot(x_vals, y_vals, 'o')
plt.plot(x_vals, y_fit)
plt.show(block=False)
