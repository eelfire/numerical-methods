import numpy as np

def lagrange(x, y, x0):
    n = len(x)
    p = 0
    for i in range(0, n):
        l = 1
        for j in range(0, n):
            if i != j:
                l = l * (x0 - x[j])/(x[i] - x[j])
        p = p + y[i]*l
    return p

x = np.array([700, 720, 740, 760, 780])
y = np.array([0.0977, 0.12184, 0.14060, 0.15509, 0.16643])
x0 = 750

print("at T = 750 F, v =", lagrange(x, y, x0))
