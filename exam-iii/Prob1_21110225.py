import numpy as np
import matplotlib.pyplot as plt

# X(t) = x(t)
# C(t) = y(t)
# S(t) = z(t)

def f(x, y, z, d):
    mu_max = 10/d
    K = 10
    Ks = 10
    kd = 0.1/d
    ke = 0.1/d
    kh = 0.1/d
    x_dot = mu_max * (1-x/K) * (z/(z+Ks)) * x - kd*x - ke*x
    y_dot = kd*x - kh*y
    z_dot = ke*x + kh*y - (mu_max * (1-x/K) * (z/(z+Ks)) * x)
    return x_dot, y_dot, z_dot

def rk4(x, y, z, d, dt):
    k1 = dt * np.array(f(x, y, z, d))
    k2 = dt * np.array(f(x + k1[0]/2, y + k1[1]/2, z + k1[2]/2, d))
    k3 = dt * np.array(f(x + k2[0]/2, y + k2[1]/2, z + k2[2]/2, d))
    k4 = dt * np.array(f(x + k3[0], y + k3[1], z + k3[2], d))
    x += (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6
    y += (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6
    z += (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6
    return x, y, z

d = 1
dt = 0.001*d
t = np.arange(0, 5*d, dt)
x0, y0, z0 = 1, 0, 100
x, y, z = x0, y0, z0

x_values = np.zeros_like(t)
y_values = np.zeros_like(t)
z_values = np.zeros_like(t)
for i in range(len(t)):
    x_values[i], y_values[i], z_values[i] = x, y, z
    x, y, z = rk4(x, y, z, d, dt)

# plt.plot(t, x_values)
# plt.plot(t, y_values)
plt.plot(t, z_values)
# plt.xlabel('t')
# plt.ylabel('x')
plt.legend(['X', 'C', 'S'])
plt.show()