#root_finding

from math import *
from pylab import *
from timeit import default_timer as timer


def f(x):
    f = (x**3)-5*x
    return f

x = arange(-10.0, 10.1, 0.1)
y=[]

for i in range(len(x)):
    y.append(f(x[i]))

plot(x,y)

"bracketing method to find ALL roots"

range_of_interest = [-10.,9.]

a= range_of_interest[0]
b= range_of_interest[1]
tol = 1e-6

def bisect(a,b,tol):
    c = (a+b)/2
    count = 0
    #print a
    #print b

    while abs(f(c)) > tol:
        count += 1
        if count > 100:
            break
        elif f(a)*f(c) < 0:
            b=c
        else:
            a=c
        c = (a+b)/2

    if abs(f(c)) < tol:
        ans = round(c,3)
        return ans
    elif f(c) == 0:
        ans = round(c,3)
        return ans

sol_list = []
start1 = timer()
for i in range(50):
    sol_list.append(bisect(uniform(a,b), uniform(a,b), tol))

#print sol_list

mylist = list(set(sol_list))

for i in range(len(mylist)):
    if mylist[i] == None:
        term = i
del mylist[term]
    
        
finish1 = timer()-start1

print 'sulutions=', mylist
print 'computation time=', finish1




