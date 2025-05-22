import numpy as np
import matplotlib.pyplot as plt

# RK4 step (modificeret til ét enkelt skridt)
def RK4_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)
    y_1 = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return y_1, t + h

# Parameters
g = 9.81
#c = 0.01
c = 0 

# Initial conditions
x10 = 0
x20 = 40

# Time parameters
t_start = 0.0
t_stop = 8.0
N = 25
t_step = (t_stop - t_start)/N
T = np.linspace(t_start, t_stop, N+1)

# System of ODEs
def fun(t, x):
    return np.array([x[1], -g - c*x[1]**2*np.sign(x[1])])

# Løsningsvektorer
X1 = np.zeros(N + 1)
X2 = np.zeros(N + 1)
X1[0] = x10
X2[0] = x20

# Startværdi
t = t_start

# Løs med RK4
for k in range(N):
    y, t = RK4_step(fun, t, np.array([X1[k], X2[k]]), t_step)
    X1[k+1] = y[0]
    X2[k+1] = y[1]

# Plot
plt.plot(T, X1, 'r-', label='z(t)')
plt.plot(T, X2, 'b-', label='v(t)')
plt.xlabel("Tid t")
plt.title("RK4 løsning for z(t) og v(t)")
plt.grid()
plt.legend()
plt.show()