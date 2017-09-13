from math import *
from numpy import *
from pylab import *

v_0 = array([1,1,1])
M = array([[0, -1, -1],
          [1, 0, -1],
          [-2, -1, 0]])
d = array([-1, -8, -14])
a = array([1./3, 1./4, 1./5])

def f(v_0):
    v_1 = a*(dot(M, v_0)+d)
    return v_1

v_1 = f(v_0)
print('0: ', v_0)
print('1: ', v_1)

i=1
while norm(v_1-v_0)>0.001:
    i += 1
    v_0 = v_1
    v_1 = f(v_0)
    print('{}: '.format(i), v_1,) 

print('converged')

i = 1
def func(x,y,z):
    global i
    xn = 1./3*(-1 -y -z)
    yn = 1./4*(-8 +xn -z)
    zn = 1./5*(-14 -2*xn -yn)
    print('{}: '.format(i), [xn, yn, zn])
    i += 1
    
    return xn, yn, zn

print('0: ', [1,1,1] )
func(1,1,1)








