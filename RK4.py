import numpy as np

def RK4(f, x0, y0, x_final, N):
    h = (x_final - x0)/N
    x = [x0]; y = [y0]
    xn = x0; yn = y0
    for k in range(N):
        k1 = f(xn,yn)
        k2 = f(xn + h/2,yn + h*k1/2)
        k3 = f(xn + h/2,yn + h*k2/2)
        k4 = f(xn + h,yn + h*k3)
        xn = xn + h
        yn = yn + h*(k1 + 2*(k2 + k3) + k4)/6
        x.append(xn); y.append(yn);
    return np.array(x), np.array(y)