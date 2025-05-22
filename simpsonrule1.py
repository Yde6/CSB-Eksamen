# Simpson (S_{2N}) sammensatte kvadraturregel (naiv implementation)

import numpy as np

def simpsonrule(f,a,b,N):
    h = (b - a)/N # bemærk: Dette er dobbelt afstanden mellem kvadraturpunkterne
    xL = a - h
    xR = a
    I = 0
    for k in range(N):
        xL = xL + h
        xR = xR + h
        I = I + h*(f(xL)+4.0*f((xL+xR)/2.0)+f(xR))/6.0 # Bemærk: Division med 6, da vi bruger h
    return I
    

def fun(x):
    if x <= np.sqrt(3):
        return -(x-np.sqrt(3))**2
    else:
        return (x-np.sqrt(3))**2

Iexact = 18-11*np.sqrt(3)
    
iter_max = 15

L0 = [0.0 for i in range(iter_max)]
L1 = [0.0 for i in range(iter_max)]
L2 = [0.0 for i in range(iter_max)]
L3 = [0.0 for i in range(iter_max)]
a = 0.0
b = 3.0

for k in range(iter_max):
    N = 2**(k+1)
    L0[k] = N
    J = simpsonrule(fun, a, b, N) 
    L1[k] = J
    L2[k] = abs(J - Iexact)
    if k>0:
        L3[k] = L2[k-1]/L2[k]

L = zip(L0,L1,L2,L3)

header_fmt='{0:^7} {1:^16} {2:^9} {3:^8}'
print(header_fmt.format('N', 'Approksimation', 'Fejl', 'Orden'))
print(header_fmt.format('-'*7, '-'*16, '-'*9, '-'*8))

for n, Z, fejl, ord in L:
    print('{0:>7} {1:<11.10E} {2:4.3E} {3:4.3E}'.format(n, Z, fejl, ord))
