# -*- coding: utf-8 -*-
from math import sin
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

# Interpolating polynomial
def lagrange(x, x_values, y_values): 
    # Lagrange basis polynomials
    def l(k, x):
        temp = [(x - x_values[j]) / (x_values[k] - x_values[j])
                for j in range(len(x_values)) if j != k]
        result = reduce(lambda x, y: x * y, temp)
        return result

    # Lagrange interpolation polynomial
    p = []
    for i in range(len(x)):
        temp = [y_values[k] * l(k, x[i]) for k in range(len(x_values))]
        p.append(sum(temp))
    return p

# Parameters for the experiment
a = 0
b = 3

def f(x):
    return x**2 - sin(10 * x)

# Error bound for equidistant points for the function f(x)=x^2-sin(10x)
def equi_bound(h, N):
    M = 10**(N + 1)
    return 0.25 * h**(N + 1) * M

# Print the results
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

for N in range(2, 91, 2):

    # Parameters for Lagrange interpolation
    h = abs(b - a) / N
    x_values = [a + k * h for k in range(N + 1)]
    y_values = [f(x) for x in x_values]

    # Points for evaluation
    N_test = 797
    x_test = np.linspace(a, b, N_test + 1)
    y_test = [f(x) for x in x_test]
    approx = lagrange(x_test, x_values, y_values)

    # Error calculation
    error = max(abs(fx - px) for fx, px in zip(y_test, approx))

    # Print table
    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, equi_bound(h, N), error))

    # Plot only for small N
    if N in [4, 6, 10]:
        plt.figure(figsize=(8, 5))
        plt.plot(x_test, y_test, label='f(x)', color='blue')
        plt.plot(x_test, approx, label='p(x)', linestyle='--', color='red')
        plt.plot(x_values, y_values, 'ko', label='Knudepunkter')
        plt.title(f'Lagrange interpolation, N = {N}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
