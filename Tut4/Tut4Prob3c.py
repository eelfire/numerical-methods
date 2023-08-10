import numpy as np
import matplotlib.pyplot as plt

N = 16

def f(x):
    return 1/(1 + 16*x**2)

def xj(j, N):
    return np.cos(j*np.pi/N)

x_data = [xj(j,N) for j in range(N+1)]
print("x_data = ", x_data)

for i in range(len(x_data)):
    print(f"f({x_data[i]}) = {f(x_data[i])}")

# for j in range(N+1):
#     print(f"f({xj(j, N)}) = {f(xj(j, N))}")
