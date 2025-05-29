import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def fuction(r, x):
    return r * x * (1.0 - x)

# Parameter
r = 3

# Generate x values
x = np.linspace(0.0, 1, 100)
y = fuction(r, x)

# Plotting
plt.figure(figsize=(6, 6))
plt.title(f'f(x) = {r} x (1 - x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0, 1)

# Plot function
plt.plot(x, y, label='f(x) = r x (1 - x)')

# Limits til plot
if r > 0:
    plt.ylim(0, max(1, y.max()))
elif r < 0:
    plt.ylim(min(-1, y.min()), 0)
else:
    plt.ylim(0, 1)  # Special case when r = 0, f(x) is constant 0

plt.grid(True)
plt.show()
