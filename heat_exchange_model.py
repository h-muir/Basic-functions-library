# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 08:49:58 2015
"""
import nelmin
import numpy as np
import scipy
import matplotlib.pyplot as plt

# Import data
tk = np.arange(0,32,2)
yk = [-0.036,-0.098,1.386,3.577,4.950,5.794,6.317,6.671,
      6.854,6.948,7.025,7.211,7.159,7.087,7.203,7.242]

N = len(tk)


# Define the function for fitting
def f(x):
    # Initial sum of error is zero - to be added to
    sum_error_squared=0
    # Loop through each data point
    for i in range (N):
        # Evaluate the function given x
        t = tk[i]
        if t > x[1]:
            y = x[0]*(1-exp(-1*(t-x[1])/x[1]))
            error_squared = (y - yk[i])**2
            sum_error_squared += error_squared
        if t <= x[1]:
            y = 0
            error_squared = (y - yk[i])**2
            sum_error_squared += error_squared
    return sum_error_squared

# Initial guess
x = np.array([5,5,5])
res = scipy.optimize.minimize(f,x,method='Nelder-Mead', tol=1.0e-12)
coef = res.x
#res=minimize(f, x, dx=None, tol=1.0e-6,maxfe=300, n_check=50, delta=0.001, Kreflect=1.0, Kextend=1.0, Kcontract=0.5)
#coef = res[0]

print(res)

# Plot the solution curve
ans = []
a, Td, tau = coef[0], coef[1], coef[2]
x = np.linspace(0,30,50)
for i in range(len(x)):
    if x[i] < Td:
        y = 0.
    else:    
        y = a*(1-exp(-1*(x[i]-Td)/tau))
    ans.append(y)

fig = plt.figure()
plt.plot(tk,yk,'o', label='Sampled data points')
plt.plot(x, ans, label='Fitted Curve')
plt.xlabel('Time (mins)')
plt.ylabel('Temperature (degrees)')
plt.title('Measured and fitted data for temperature response to a step function input in a heat exchanger')
fig.patch.set_facecolor('white')
plt.legend(loc='lower right')
plt.show(block=False)


