# Import modules
from numpy import *
from pylab import *

# Define function to iterate
def g(x):
	return cos(x)

# Define interval (a,b) for iteration and mesh
a = 0
b = 3

# Setup x array
x = linspace(0, 3, 200, endpoint=True)

# Initial value
x_init = 0.1

# Setup the plot
figure(1, (6,6))
title('Solving $x=\cos(x)$ by iteration')
xlabel('X(n)')
ylabel('X(n+1)')

# Plot identity line y = x
plot(x, x, 'b--', label='$y = x$', antialiased=True)

# Plot y = g(x)
plot(x, g(x), 'g', label='$g(x)$', antialiased=True)

# Plot f(x) = cos(x) - x
plot(x, g(x) - x, 'm', label='$f(x)$')

# Set initial condition
state = x_init
x0 = []
x1 = []

# Iterate and store lines for cobweb
nIterates = 15
for n in range(nIterates):
	x0.append(state)
	x1.append(state)
	x0.append(state)
	state = g(state)
	x1.append(state)

# Plot cobweb lines and starting point
plot(x0, x1, 'r', label='Iteration', antialiased=True)
plot(x_init, x_init, '.k', label='Start')

legend()
grid(True)
xlim(0, 1.5)
ylim(0, 1.5)
show()

