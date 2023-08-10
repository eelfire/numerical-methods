import numpy as np

y = np.array([0., 1., 3., 5., 7., 8., 9., 10.])
H = np.array([0., 1., 1.5, 3., 3.5, 3.2, 2., 0.])
U = np.array([0., 0.09, 0.12, 0.23, 0.243, 0.27, 0.18, 0])

flow_rate = []
for j in range(len(y)):
    flow_rate.append(H[j]*U[j])

# def trapezoid_rule(f,a):
#     ln = len(a)
#     integral = 0.

#     for i in range(ln-1):
#         integral += (f[i+1] - f[i]) * (a[i] + a[i+1]) / 2
#     integral += (f[ln-1] - f[0]) * (a[0] + a[ln-1]) / 2

#     return integral

def trapezoidal(f, num_interval, x_data):
    h = (x_data[-1] - x_data[0])/num_interval
    sum = 0
    for i in range(1, num_interval):
        sum += f[x_data[i]]
    return h/2*(f[x_data[0]] + 2*sum + f[x_data[-1]])

a = min(y)
b = max(y)
n = len(y)

H_avg = (1/(b-a)) * trapezoidal(H,n,y)

Ac = trapezoidal(H,n,y)

Q = trapezoidal(flow_rate,n,y)

print("Average Depth:", H_avg)
print("Cross-Sectional area:", Ac)
print("Flow Rate:", Q)