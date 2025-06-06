# Adaptiv Simpson. Naiv implementation der ikke bekymrer sig om genbrug af 
# funktionsevalueringer.

import numpy as np
import matplotlib.pyplot as plt

# implementation af S_{2N} fra kursusgang 7
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

# global variabel til at gemme kvadraturpunkter, bruges KUN til plot
quadpoints = []; 
  
def adaptivestep(f,xL,xR,tol):
    S2 = simpsonrule(f,xL,xR,1)
    S4 = simpsonrule(f,xL,xR,2)
    xM = (xL+xR)/2
    quadpoints.append(xM) # bruges kun til plot
    if abs(S4-S2) <= 15*tol: # bemærk at faktoren 15 er specifik for Simpons regel
        quadpoints.append((xL+xM)/2) # bruges kun til plot
        quadpoints.append((xM+xR)/2) # bruges kun til plot
        return S4 # denne approksimation har fejl ca. tol/(2^k) på delintervallet
    else:
        return adaptivestep(f,xL,xM,tol/2) + adaptivestep(f,xM,xR,tol/2)

def adaptivesimpson(f,a,b,tol):
    quadpoints.append(a) # bruges kun til plot
    quadpoints.append(b) # bruges kun til plot
    return adaptivestep(f,a,b,tol)

def fun(x):
    x = np.asarray(x)  # konverter input til array hvis det ikke er det
    return np.where(x <= np.sqrt(3),
                    -(x - np.sqrt(3))**2,
                     (x - np.sqrt(3))**2)
Iexact = 18-11*np.sqrt(3)
    
a = 0
b = 3
# Pas på med for lav tolerance: Der er ikke sat et maksimum på antallet af 
# inddelinger, så ved meget lav tolerance kan afrundingsfejl gøre at den 
# rekursive inddeling ikke kan opnå tolerancen. 
tol = 1e-15

J = adaptivesimpson(fun, a, b, tol)
print('Fejl: ',abs(Iexact-J))
print('Antal indelinger: ', len(quadpoints)-1)

# plot af kvadraturpunkter
quadpoints = np.sort(np.array(quadpoints));
x = np.linspace(a,b,500);
plt.figure()
plt.plot([a,b],[0,0],'k--')
plt.plot(x,fun(x),'b-')
plt.plot(quadpoints,fun(quadpoints),'r.')
plt.xlim([a,b])
plt.title(f'Adaptiv Simpson regel for [{a} ; {b}]')
fejl = abs(Iexact - J)
antal = len(quadpoints) - 1

plt.show()
