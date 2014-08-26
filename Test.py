from numpy import linalg as la
import numpy as np

#random initialization of a tensor with comlex entries
a = np.matrix("4 3 5; 6 7 8; 1 3 13; 7 21 9.0")
v = np.matrix("1;2;3");
b = a.T

w,v = la.eig(a*b)


