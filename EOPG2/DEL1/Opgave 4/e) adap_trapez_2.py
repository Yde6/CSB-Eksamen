import numpy as np
import matplotlib.pyplot as plt

# implementation af trapezreglen
def trapezoidalrule(f,a,b,N):
    h = (b - a)/N
    xL = a - h
    xR = a
    I = 0
    for k in range(N):
        xL = xL + h
        xR = xR + h
        I = I + h*(f(xL)+f(xR))/2.0
    return I

# global variabel til at gemme kvadraturpunkter, bruges KUN til plot
quadpoints = []; 
  
def adaptivestep(f,xL,xR,tol):
    T1 = trapezoidalrule(f,xL,xR,1)
    T2 = trapezoidalrule(f,xL,xR,2)
    xM = (xL+xR)/2
    quadpoints.append(xM) # bruges kun til plot
    # Fejlestimat: Trapezreglen har 1. orden fejl, faktor 3 bruges her som heuristik
    if abs(T2 - T1) <= 15*tol: 
        quadpoints.append((xL+xM)/2) # bruges kun til plot
        quadpoints.append((xM+xR)/2) # bruges kun til plot
        return T2 
    else:
        return adaptivestep(f,xL,xM,tol/2) + adaptivestep(f,xM,xR,tol/2)

def adaptivetrapezoid(f,a,b,tol):
    quadpoints.append(a) # bruges kun til plot
    quadpoints.append(b) # bruges kun til plot
    return adaptivestep(f,a,b,tol)

def fun(x):
    x = np.asarray(x)  # konverter input til array hvis det ikke er det
    return np.where(x <= np.sqrt(3),
                    -(x - np.sqrt(3))**2,
                     (x - np.sqrt(3))**2)
    

Iexact = 18 - 11*np.sqrt(3) # For hele intervallet
#Iexact = -1.727885683 # For intervallet [0;1.5]
#Iexact = 0.6753267990 #For intervallet [1.5;3]

a = 0
b = 3
tol = 1e-3

J = adaptivetrapezoid(fun, a, b, tol)
print('Fejl: ',abs(Iexact - J))
print('Antal inddelinger: ', len(quadpoints) - 1)

# plot af kvadraturpunkter
quadpoints = np.sort(np.array(quadpoints));
x = np.linspace(a, b, 500)
plt.figure()
plt.plot([a, b], [0, 0], 'k--')
plt.plot(x, fun(x), 'b-')
plt.plot(quadpoints, fun(quadpoints), 'r.')
plt.xlim([a, b])
plt.title(f'Adaptiv Trapezregel for [{a};{b}]')
plt.show()
