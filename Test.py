from numpy import linalg as la
import numpy as np
import matplotlib.pyplot as plt #our shortcut

#random initialization of a tensor with comlex entries
a = np.matrix("4 3 5; 6 7 8; 1 3 13; 7 21 9.0")
v = np.matrix("1;2;3");
b = a.T

w,v = la.eig(a*b)

b = w.T

#def fib(n): 
#    return 2*n
    
c = np.linspace(0,5,6)

a = np.sqrt(c)
print(a)

x = numpy.linspace(0,5,20)      #create our first array
y = x**2    #this is how Python does exponents

plt.plot(x,y)           #create the plot
plt.show()              #show the plot

