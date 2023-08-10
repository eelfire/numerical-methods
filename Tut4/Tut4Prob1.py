# The outflow concentration from a reactor is measured at discrete times over a 24-hr period and the values are as follows:

import numpy as np

num_interval = 5000
y = 24
x_data = np.linspace(0, y, num_interval+1)

def Q(x):
    return 20 + 10*np.sin(2*np.pi/24*(x - 10))

def lagrange(x, x_data, y_data):
    sum = 0
    for i in range(len(x_data)):
        product = 1
        for j in range(len(x_data)):
            if j != i:
                product *= (x - x_data[j])/(x_data[i] - x_data[j])
        sum += product*y_data[i]
    return sum

def c(x):
    t = np.array([0, 1, 5.5, 10, 12, 14, 16, 18, 20, 24])
    c = np.array([1, 1.5, 2.3, 2.1, 4, 5, 5.5, 5, 3, 1.2])
    return lagrange(x, t, c)

def f(x):
    return c(x)*Q(x)

def f2(x):
    return Q(x)

def trapezoidal(f, num_interval, x_data):
    h = (x_data[-1] - x_data[0])/num_interval
    sum = 0
    for i in range(1, num_interval):
        sum += f(x_data[i])
    return h/2*(f(x_data[0]) + 2*sum + f(x_data[-1]))

def simpson(f, num_interval, x_data):
    h = (x_data[-1] - x_data[0])/num_interval
    sum = 0
    for i in range(1, num_interval):
        if i % 2 == 0:
            sum += 2*f(x_data[i])
        else:
            sum += 4*f(x_data[i])
    return h/3*(f(x_data[0]) + sum + f(x_data[-1]))

print("Trapezoidal: ", trapezoidal(f, num_interval, x_data)/trapezoidal(f2, num_interval, x_data))
print("Simpson's 1/3: ", simpson(f, num_interval, x_data)/simpson(f2, num_interval, x_data))