#runge-kutta example

from math import *
from numpy import *
from pylab import *

"runge-kutta function"

def runge(f, x0, t0):
    t = []
    f_of_t = []
    t_range = [1,6]
    h = 1.
    wi = x0
    for i in list(arange(1,7,h)):
        t.append(i)
        f_of_t.append(wi)
        ti = i
        k1 = h*f(ti, wi)
        k2 = h*f(ti+h/2, wi+k1/2)
        k3 = h*f(ti+h/2, wi+k2/2)
        k4 = h*f(ti+h, wi+k3)
        print(wi)
        wi += (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return t, f_of_t


"ode function"

def f(t,x): #f-dash
    return 1+x/t

#intitial conditions:
x0 = 1
t0 = 1

t, f_of_t = runge(f, x0, t0)

"analytic solution"
def f_of_x(t):
    return t*(1+log(t))

x = list(arange(1.,6.1,0.1))
y = []
for i in x:
    y.append(f_of_x(i))

figure(1)
plot(t, f_of_t, 'o')
hold = True
plot(x,y)
hold = False
show(block=True)
