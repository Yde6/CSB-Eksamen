from math import sin
import matplotlib.pyplot as plt

# Interpolating polynomial
def lagrange(x, x_values, y_values): 
    
    from functools import reduce
    # Lagrange basis polynomials
    def l(k,x):
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k]
        result = reduce(lambda x, y: x*y, temp)
        return result
    
    # Lagrange interpolation polynomial
    p = []
    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))
    
    return p

# Parameters for the experiment
a = 0
b = 3

def f(x):
    return x**2-sin(10*x)

# Error bound for equidistant points for the function f(x)=x^2-sin(10x)
def equi_bound(h, N):
    M = 10**(N+1)
    return 0.25*h**(N+1)*M

# Values of N to test
N_values = [5, 10, 20, 30, 40]

# Set up the plot
plt.figure(figsize=(12, 8))

# Print the results
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

x_plot = [a + k*(b-a)/1000 for k in range(1001)]
y_plot = [f(x) for x in x_plot]
plt.plot(x_plot, y_plot, label="Original f(x)", color="black", linewidth=2)

for N in N_values:
    
    # Parameters for Lagrange interpolation
    h = abs(b-a)/N
    x_values = [a+k*h for k in range(N+1)] 
    y_values = [f(x_values[k]) for k in range(N+1)]
   
    # New points for calculating the error max|f(x)-p_N(x)|
    N_test = 797 
    h_test = abs(b-a)/N_test
    x_test = [a+k*h_test for k in range(N_test+1)]
     
    # Calculate the approximation and the solution
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    # Calculate the error
    from operator import sub
    temp1 = list(map(sub, y_test, approx))
    temp2 = list(map(abs, temp1))
    error = max(temp2)
    
    # Print a table
    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, \
          equi_bound(h,N), error))
    
    # Plot the error
    plt.plot(x_test, approx, label=f'N={N}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Error |f(x) - p_N(x)|')
plt.title('Error |f(x) - p_N(x)| for Different Values of N')
plt.legend()
plt.grid(True)
plt.show()
