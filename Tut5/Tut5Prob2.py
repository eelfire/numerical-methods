import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma, b, r):
    x_dot = -sigma*x + sigma*y
    y_dot = r*x - y - x*z
    z_dot = -b*z + x*y
    return x_dot, y_dot, z_dot

def rk4(x, y, z, sigma, b, r, dt):
    k1 = dt * np.array(lorenz(x, y, z, sigma, b, r))
    k2 = dt * np.array(lorenz(x + k1[0]/2, y + k1[1]/2, z + k1[2]/2, sigma, b, r))
    k3 = dt * np.array(lorenz(x + k2[0]/2, y + k2[1]/2, z + k2[2]/2, sigma, b, r))
    k4 = dt * np.array(lorenz(x + k3[0], y + k3[1], z + k3[2], sigma, b, r))
    x += (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6
    y += (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6
    z += (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6
    return x, y, z

sigma = 10
b = 2.67
r = 28
x, y, z = 5, 5, 5
dt = 0.01
t = np.arange(0, 20, dt)

x_values = np.zeros_like(t)
y_values = np.zeros_like(t)
z_values = np.zeros_like(t)
for i in range(len(t)):
    x_values[i], y_values[i], z_values[i] = x, y, z
    x, y, z = rk4(x, y, z, sigma, b, r, dt)

plt.figure(figsize=(10,10))
plt.subplot(221)
plt.plot(t, x_values, 'r')
plt.xlabel('t')
plt.ylabel('x')
plt.subplot(222)
plt.plot(t, y_values, 'g')
plt.xlabel('t')
plt.ylabel('y')
plt.subplot(223)
plt.plot(t, z_values, 'b')
plt.xlabel('t')
plt.ylabel('z')
plt.subplot(224, projection='3d')
plt.plot(x_values, y_values, z_values)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
