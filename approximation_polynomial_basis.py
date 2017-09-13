from math import *
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

#Q2
data = np.loadtxt('P2_data.txt', skiprows=1)

n = 2 #order of polynomial fit

D_matrix = np.zeros((n+1,n+1))  #initialising design matrix
fx = np.zeros(n+1)              #initialising right hand side vector
x_vals = data[:,0]
y_vals = data[:,1]

#constructing matrix
for i in range(n+1):
    for j in range(n+1):
         D_matrix[i][j] = sum(x_vals**(i+j))
    fx[i] = sum(y_vals*(x_vals**i))
    
#solving for coefficients
inv_D = linalg.inv(D_matrix)
coeffs = np.dot(inv_D, fx)

#constructing fitted solution
y_fit = np.zeros(len(x_vals))
i = 0
for x in x_vals:
    y_fit[i] = coeffs[0] + coeffs[1]*x + coeffs[2]*x**2
    i += 1

plt.figure()
plt.plot(x_vals, y_vals, 'o')
plt.plot(x_vals, y_fit)
plt.show(block=False)




