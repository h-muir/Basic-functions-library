#cubic spline practise

from math import *
from numpy import *
from pylab import *

#data:

x = [1,2,3,5,6]
y = [1,3,7,15,18]

n = len(x)-2

A = zeros((n,n))
for i in range(n):
    A[i,i] = 2*(x[i+2]-x[i])
    if i != 0:
        A[i,i-1] = x[i+1]-x[i]
    if i != 2:
        A[i,i+1] = x[i+2]-x[i+1]
b = array([12, 0, -6])

sigma = solve(A,b)
sigma = [0]+list(sigma)+[0]

xs = []
ys = []
for i in range(len(x)-1):
    h = (x[i+1]-x[i])
    a = (sigma[i+1]-sigma[i])/(6*h)
    b = sigma[i]/2
    c = (y[i+1]-y[i])/(h) - h*(sigma[i+1]+2*sigma[i])/6
    d = y[i]
    for j in linspace(x[i], x[i+1], 20):
        xs.append(j)
        si = a*(j-x[i])**3 + b*(j-x[i])**2 + c*(j-x[i])+d
        ys.append(si)
"""
figure()
plot(x,y, 'o')
plot(xs,ys)
show(block=False)
"""
#bezier spline

k = len(x)

#find d points:

dx = zeros(k)
dy = zeros(k)

dx[0] = x[0]; dy[0] = y[0]
dx[-1] = x[-1]; dy[-1] = y[-1]

A = zeros((k-2,k-2))
bx = zeros((k-2))
by = zeros((k-2))
for i in range(k-2):
    if i == 0:
        bx[i] = x[i+1]-dx[0]/6
        by[i] = y[i+1]-dy[0]/6
        A[i,i] = 4
        A[i,i+1] = 1
    if i == k-3:
        bx[i] = x[i+1]-dx[-1]/6
        by[i] = y[i+1]-dy[-1]/6
        A[i,i] = 4
        A[i,i-1] = 1
    else:
        bx[i] = x[i+1]
        by[i] = y[i+1]
        A[i,i] = 4
        A[i,i-1] = 1
        A[i,i+1] = 1
A = A/6

d_midx = solve(A, bx)
d_midy = solve(A, by)

for i in range(n):
    dx[i+1] = d_midx[i]
    dy[i+1] = d_midy[i]


figure()
plot(x,y,'o')
plot(dx, dy)
show(block=False)



        
