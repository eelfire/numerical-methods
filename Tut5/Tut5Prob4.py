import numpy as np
import matplotlib.pyplot as plt

def f(t, y, w):
    return np.array([y[1], -w**2*np.sin(y[0])])

def rk4(f, t, y, h, w):
    k1 = h*f(t, y, w)
    k2 = h*f(t+h/2, y+k1/2, w)
    k3 = h*f(t+h/2, y+k2/2, w)
    k4 = h*f(t+h, y+k3, w)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6

def solve(f, t0, y0, h, w, tmax):
    t = np.arange(t0, tmax, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = rk4(f, t[i-1], y[i-1], h, w)
    return t, y

t0 = 0
y0 = np.array([-np.pi/2, 0])
h = 0.01
tmax = 15

w = [1, 2, 4, 8]

for i in range(len(w)):
    t, y = solve(f, t0, y0, h, w[i], tmax)
    plt.plot(t, y[:,0], label='w = ' + str(w[i]))
    # plt.figure(1)

plt.xlabel('t')
plt.ylabel('y')
plt.ylim(-4, 4)
plt.xlim(0, 15)
plt.legend()
plt.show()

for i in range(len(w)):
    t, y = solve(f, t0, y0, h, w[i], tmax)
    plt.plot(t, y[:,1], label='w = ' + str(w[i]))
    # plt.figure(2)

plt.xlabel('y')
plt.ylabel('dy/dt')
plt.legend()
plt.show()

