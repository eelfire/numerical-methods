import numpy as np

num_interval = 16
y = 1
x_data = np.linspace(-1, y, num_interval+1)

def f(x):
    return 1/(1 + 16*x**2)

for i in range(len(x_data)):
    print(f"f({x_data[i]}) = {f(x_data[i])}")
