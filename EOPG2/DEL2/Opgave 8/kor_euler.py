import numpy as np
import matplotlib.pyplot as plt


# Euler step
def euler(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + (h/2), y + (h * (k1/2)))
    y1 = y + h*k2
    return y1, t + h

# equation parameters
g = 9.81
#c = 0.01
c = 0

# initial conditions
x10 = 0
x20 = 40

# time parameters
t_start = 0.0
t_stop = 8.0
N = 25
t_step = (t_stop - t_start)/N
T = np.linspace(t_start, t_stop, N+1)


# The system 
def fun(t, x):
    return np.array([x[1], -g - c*x[1]**2*np.sign(x[1])])



X1 = np.zeros(N + 1)
X2 = np.zeros(N + 1)


X1[0] = x10
X2[0] = x20

# initialize time variable
t = t_start

# solve
for k in range(N):
    y, t = euler(fun, t, np.array([X1[k], X2[k]]), t_step)
    X1[k+1] = y[0]
    X2[k+1] = y[1]
    
plt.plot(T, X1, 'r-', T, X2, 'b-')
plt.grid()
plt.show()
