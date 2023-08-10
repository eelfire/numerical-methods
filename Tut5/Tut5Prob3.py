import numpy as np
import matplotlib.pyplot as plt

def f(t, y, mu):
    return np.array([y[1], mu*(1-y[0]**2)*y[1]-y[0]])

def rk4(f, t, y, h, mu):
    k1 = h*f(t, y, mu)
    k2 = h*f(t+h/2, y+k1/2, mu)
    k3 = h*f(t+h/2, y+k2/2, mu)
    k4 = h*f(t+h, y+k3, mu)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6

def solve(f, t0, y0, h, mu, tmax):
    t = np.arange(t0, tmax, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = rk4(f, t[i-1], y[i-1], h, mu)
    return t, y

t0 = 0
y0 = np.array([4, 0])
h = 0.01
tmax = 50

mu = [0.1, 1, 4.5]

for i in range(len(mu)):
    t, y = solve(f, t0, y0, h, mu[i], tmax)
    plt.plot(t, y[:,0], label='mu = ' + str(mu[i]))
    # plt.figure(1)

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

for i in range(len(mu)):
    t, y = solve(f, t0, y0, h, mu[i], tmax)
    plt.plot(y[:,0], y[:,1], label='mu = ' + str(mu[i]))
    # plt.figure(2)

plt.xlabel('y')
plt.ylabel('dy/dt')
plt.legend()
plt.show()