#bezier curves

from math import *
from numpy import *
from pylab import *


def bezier_n(P_list,t):
    n = len(P_list)
    B_t = 0
    for i in range(n):
        B_t += factorial(n-1)/(factorial(i)*factorial(n-1-i))*\
               (1-t)**(n-1-i)*t**i*P_list[i]

    return B_t

def bezier_n2(P_list,t):
    if len(P_list) == 1:
        return P_list[0]
    else:
        P_list = list((1-t)*array(P_list[0:-1]) + t*array(P_list[1:]))
        return bezier_n2(P_list,t)

if __name__ == "__main__":
    x = [1,2,3,5,6]
    y = [1,2,5,15,16]
    P_list = []
    for i in range(len(x)):
        P_list.append(array([x[i],y[i]]))


    t_list = linspace(0, 1, 50)
    xb = []
    yb = []
    for t in t_list:
        xb.append(bezier_n(P_list, t)[0])
        yb.append(bezier_n(P_list, t)[1])

    xb2 = []
    yb2 = []
    for t in t_list:
        xb2.append(bezier_n2(P_list, t)[0])
        yb2.append(bezier_n2(P_list, t)[1])

    figure()
    plot(x,y, 'o')
    plot(xb, yb, 'g')
    plot(xb2, yb2, 'go')
    show(block=False)
   
        
    
