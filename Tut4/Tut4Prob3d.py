import numpy as np
import matplotlib.pyplot as plt

N = 16

def f(x):
    return 1/(1 + 16*x**2)

def xj(j, N):
    return np.cos(j*np.pi/N)

x_data = np.array([xj(j,N) for j in range(N+1)])

x_data_np = np.linspace(-1, 1, N+1)

def lagrange(x, x_data, y_data):
    sum = 0
    for i in range(len(x_data)):
        product = 1
        for j in range(len(x_data)):
            if j != i:
                product *= (x - x_data[j])/(x_data[i] - x_data[j])
        sum += product*y_data[i]
    return sum

def g(x):
    return lagrange(x, x_data, f(x_data))

def Et(x):
    max = np.abs(f(x[0]) - g(x[0]))
    for i in range(len(x_data)):
        E_i = np.abs(f(x[i]) - g(x[i]))
        if E_i > max:
            max = E_i
    return max

print("Et,max = ", Et(x_data_np))

x = np.linspace(-1, 1, 1000)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, g(x), label="g(x)")
plt.plot(x_data, f(x_data), 'o', label="Data points")
plt.ylim(-1, 1.5)
plt.legend()
plt.show()
