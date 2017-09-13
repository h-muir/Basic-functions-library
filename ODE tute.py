#ODE Tute

from math import *
from numpy import *
from pylab import *

"Global variables"
g = 9.8
m = 200
M = 1000
L = 10

K1 = 3.
K2 = 93.0
K3 = 25150.
K4 = 23346.
"runge-kutta function"

h = 0.1

def runge1(h):
    time = [0]
    theta_dash = [0.]
    x_dash = [0.]
    theta_list = [0.1]
    x_list = [0.]
    #initial conditions:
    z1 = 0.
    z2 = 0.
    z3 = 0.1
    z4 = 0.
    for i in list(arange(h,100,h)):
        t = i
        time.append(t)
        
        k1t = h*t11(z1, z2, z3, z4)
        k1x = h*x11(z1, z2, z3, z4)
        
        k2t = h*t11(z1, z2, z3, z4+k1t/2)
        k2x = h*x11(z1, z2+k1x/2, z3, z4)
        
        k3t = h*t11(z1, z2, z3, z4+k2t/2)
        k3x = h*x11(z1, z2+k2x/2, z3, z4)
        
        k4t = h*t11(z1, z2, z3, z4+k3t)
        k4x = h*x11(z1, z2+k3x, z3, z4)

        z1 += z2*h
        x_list.append(z1)
        z2 += (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
        x_dash.append(z2)
        z3 += z4*h
        theta_list.append(z3)
        z4 += (1/6)*(k1t + 2*k2t + 2*k3t + k4t)
        theta_dash.append(z4)
        
    return time, theta_list, x_list


"ode function"

def x11(z1, z2, z3, z4):
    F = K1*z1 + K2*z2 + K3*z3 + K4*z4
    num = F - m*g*sin(z3)*cos(z3) + m*L*sin(z3)*z4**2
    denom = (M+m) - m*(cos(z3))**2
    return num/denom

def t11(z1, z2, z3, z4): #theta double dash --> theta dash
    F = K1*z1 + K2*z2 + K3*z3 + K4*z4
    num = F*cos(z3)-(M+m)*g*sin(z3)
    denom = m*L*(cos(z3))**2 - (M+m)*L
    return num/denom
               
time, theta_list, x_list = runge1(h)

assert len(time) == len(theta_list)
assert len(time) == len(x_list)

figure(1)
plot(time, theta_list)

figure(2)
plot(time, x_list)
show(block=False)
