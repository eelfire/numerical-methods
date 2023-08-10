import numpy as np

num_interval = 5000
y = 1000
x_data = np.linspace(1, y, num_interval+1)

def f(x):
    return np.exp(-x)/x

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

print("Trapezoidal: ", trapezoidal(f, num_interval, x_data))
print("Simpson's 1/3: ", simpson(f, num_interval, x_data))
