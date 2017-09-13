from math import *
from numpy import *
from pylab import *


def f(x):
    return exp(x)-3*cos(x)

def f_dash(x):
    return exp(x) + 3*sin(x)

x0 = 1
print('it. 0: x = {}, f(x) = {}'.format(x0, f(x0))) 

def update(x):
    x_new = x - f(x)/f_dash(x)
    return x_new

x_new = update(x0)
print('it. 1: x = {}, f(x) = {}'.format(x_new, f(x_new))) 

x = x0
i = 1
while abs(x_new - x) > 0.001:
    i+=1
    x = x_new
    x_new = update(x)
    print('it. {}: x = {}, f(x) = {}'.format(i, x_new, f(x_new)))


print('done.')


    
    
