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

x = np.array([0, 6, 10, 13, 17, 20, 28])
y1 = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])
y2 = np.array([6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89])
x0 = 12
x1 = 16

print("Sample 1, Day 12: Avg weight =", lagrange(x, y1, x0))
print("Sample 2, Day 12: Avg weight =", lagrange(x, y2, x0))
print("Sample 1, Day 16: Avg weight =", lagrange(x, y1, x1))
print("Sample 2, Day 16: Avg weight =", lagrange(x, y2, x1))