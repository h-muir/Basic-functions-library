from math import *
import numpy as np
import matplotlib.pyplot as plt

#1: calculat n!

def n_factorial(n):
    f = 1
    assert n>=0
    for i in np.arange(1,n+1,1):
        f *= i
    return f

#2: taylor series of exp(x)

def exp_taylor(h, n):
    t_sum = 0
    for i in range(n):
        t_i = h**i/n_factorial(i)
        t_sum += t_i
    t_err = h**n/n_factorial(n)
    
    return t_sum, t_err

#4: plotting
d = 50 #discretisation
x_list = np.linspace(-2, 2, d)
exp_y = np.zeros(d)
for i, x in enumerate(x_list):
    exp_y[i] = exp(x) 

exp_taylor_y = np.zeros(d)
def gen_exp_taylor(x_list, n):
    d = len(x_list)
    exp_taylor_list = np.zeros(d)
    error_list = np.zeros(d)
    i = 0
    for x in x_list:
        exp_taylor_list[i], error_list[i] = exp_taylor(x, n)
        i += 1
    abs_error_list = exp_y - exp_taylor_list
    return exp_taylor_list, error_list, abs_error_list

#plt.figure()
f, ax = plt.subplots(1,2)
plt.suptitle('Taylor series approximations of exp(x)')
ax[0].plot(x_list, exp_y, 'k', label="in-built")
ax[0].plot(x_list, gen_exp_taylor(x_list, 2)[0], 'm', label="n=2")
ax[0].plot(x_list, gen_exp_taylor(x_list, 3)[0], 'g', label="n=3")
ax[0].plot(x_list, gen_exp_taylor(x_list, 4)[0], 'b', label="n=4")
ax[0].plot(x_list, gen_exp_taylor(x_list, 6)[0], '0.7', label="n=6")
ax[0].legend(loc='best')
ax[1].plot(x_list, gen_exp_taylor(x_list, 2)[1], 'm', label="n=2")
ax[1].plot(x_list, gen_exp_taylor(x_list, 3)[1], 'g', label="n=3")
ax[1].plot(x_list, gen_exp_taylor(x_list, 4)[1], 'b', label="n=4")
ax[1].plot(x_list, gen_exp_taylor(x_list, 6)[1], '0.7', label="n=6")
ax[1].plot(x_list, gen_exp_taylor(x_list, 2)[2], 'm--')
ax[1].plot(x_list, gen_exp_taylor(x_list, 3)[2], 'g--')
ax[1].plot(x_list, gen_exp_taylor(x_list, 4)[2], 'b--')
ax[1].plot(x_list, gen_exp_taylor(x_list, 6)[2], '0.7')
ax[1].legend(loc='best')
plt.show(block=False)


        
    




