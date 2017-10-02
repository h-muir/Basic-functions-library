#1D wave equation PDE solution

from math import *
from numpy import *
from pylab import *

from mpl_toolkits.mplot3d import Axes3D

dx = 0.1
dt = 0.005
beta = 4
x0 = arange(0, 2+dx, dx)
nx = len(x0)
nt = 100
print("total time = ", dt*nt)

G = beta*dt**2/dx**2

u0 = zeros(nx)
u0t = zeros(nx)
for i, x in enumerate(x0):
    u0[i] = 0.1*sin(pi*x)
    u0t[i] = 0.2*pi*sin(pi*x)
u1 = u0 + u0t*dt

D_matrix = zeros((nx, nx))
for i in range(nx):
    if i != 0:
        D_matrix[i][i-1] = G
        
    D_matrix[i][i] = 2-2*G
    
    if i != nx-1:
        D_matrix[i][i+1] = G

u_set = zeros((nt, nx))
u_set[0] = u0
u_set[1] = u1
u_prev = u0
u_i = u1

for i in range(2, nt):
    u_next = dot(D_matrix, u_i) - u_prev
    u_set[i] = u_next
    #enforce end conditions:
    u_next[0] = 0
    u_next[-1] = 0
    #----------------
    u_prev = u_i
    u_i = u_next

figure()
plot(x0, u0)
plot(x0, u1)
for i in range(2, nt):
    if i%5 == 0:
        plot(x0, u_set[i], 'k')
show(block=False)

X_set = zeros((nt, nx))
Y_set = zeros((nt, nx))
for i in range(nt):
    X_set[i] = x0
    Y_set[i] = array([dt]*nx)*i

y0 = arange(0, dt*nt, dt)
X, Y = meshgrid(x0, y0)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X=X, Y=Y, Z=u_set)
show(block=False)



