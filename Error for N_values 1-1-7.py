import matplotlib.pyplot as plt

import decimal
context = decimal.getcontext()  # Get the current default context
digits = 40                     # Significant digits
context.prec = digits           
D = decimal.Decimal             # Construct a new Decimal object

# A version of pi for decimal computation from decimal documentation
def Dpi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = D(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s               # unary plus applies the new precision


# A version of sin for decimal computation from decimal documentation
def Dsin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)
    """
    decimal.getcontext().prec += 2
    x = x % (2 * Dpi())
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s

def Dcos(x):
    """Return the cosine of x as measured in radians using the Taylor series expansion."""
    decimal.getcontext().prec += 2  # Increase precision for intermediate steps
    x = x % (2 * Dpi())  # Normalize x to the range [0, 2π]
    
    i, lasts, s, fact, num, sign = 0, 0, D(1), 1, D(1), 1
    while s != lasts:  # Loop until the result stabilizes
        lasts = s
        i += 2
        fact *= i * (i - 1)  # Calculate factorial (2n)!
        num *= x * x  # Calculate x^2, x^4, x^6, etc.
        sign *= -1  # Alternate signs for the series terms
        s += num / fact * sign  # Add the next term in the series
    
    decimal.getcontext().prec -= 2  # Restore the default precision
    return +s  # Apply the new precision and return the result

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

# Error bound for equidistant points for the function f(x)=x^2-sin(10x)
def equi_bound(h, N):
    M = D(10)**(N+1)
    return D(0.25)*h**(N+1)*M


# Parameters for the experiment
def f(x):
    return x**2-Dsin(D(10)*x)

a = D(0)
b = D(3)


# Values of N to test
N_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Set up the plot
plt.figure(figsize=(12, 8))

# Print the results
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('          Precision = ',digits) # print precision
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

x_plot = [a + k*(b-a)/1000 for k in range(1001)]
y_plot = [f(x) for x in x_plot]
plt.plot(x_plot, y_plot, label="Original f(x)", color="black", linewidth=2)

for N in N_values:
    
    # Parameters for Lagrange interpolation
    h = abs(b-a)/D(N)
    x_values = [a + (b - a) * (1 - Dcos(Dpi() * (j / D(N)))) / 2 for j in range(N + 1)] 
    y_values = [f(x_values[k]) for k in range(N+1)]
   
    # New points for calculating the error max|f(x)-p_N(x)|
    N_test = 797 # 1297
    h_test = abs(b-a)/D(N_test)
    x_test = [a+k*h_test for k in range(N_test+1)]
     
    # Calculate the approximation and the solution
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    # Calculate the error
    from operator import sub, abs
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