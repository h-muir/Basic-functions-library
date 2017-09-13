from math import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np

def f0(x):
    return sin(x)

def f1(x):
    return cos(x)

def f2(x):
    return -sin(x)

def f3(x):
    return -cos(x)

f_dash = {0 : f0,
          1 : f1,
          2 : f2,
          3 : f3}

def recursive_taylor(x, h, n):
    t=0
    for i in range(n):
        eq_no = i%4
        ti = h**i/factorial(i) * f_dash[eq_no](x)
        t += ti

    e_est = h**(n+1)/factorial(n+1) * f_dash[(n+1)%4](x)
    return t, e_est


h_list = np.linspace(-pi, pi, 50)
sin_wave = f0(h_list)
taylor_list = [0]*50
e_list = [0]*50

i=0
for h in h_list:
    taylor_list[i], e_list[i] = recursive_taylor(0,h,8)
    i += 1

actual_e = array(taylor_list)-array(sin_wave)

print("calcs done")

f, axes = subplots(1,2)
#figure()
axes[0].plot(h_list, sin_wave) 
axes[0].plot(h_list, taylor_list)


#figure()
axes[1].plot(h_list, actual_e)
axes[1].plot(h_list, array(e_list))
axes[1].plot(h_list, abs(actual_e - array(e_list)))
show(block=False)

