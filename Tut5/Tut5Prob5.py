import numpy as np
import matplotlib.pyplot as plt

def gauss_elim(A, b):
    n = len(b)
    aug_matrix = np.hstack((A, b.reshape(n,1)))
    for i in range(0, n-1):
        for j in range(i+1, n):
            scaling_factor = aug_matrix[j][i]/aug_matrix[i][i]
            aug_matrix[j] = aug_matrix[j] - (scaling_factor * aug_matrix[i])
    x = np.zeros(n)
    x[n-1] = aug_matrix[n-1][n]/aug_matrix[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = aug_matrix[i][n]
        for j in range(i+1, n):
            x[i] = x[i] - aug_matrix[i][j]*x[j]
        x[i] = x[i]/aug_matrix[i][i]
    return x

def solve(N, p):
    ul = 0
    ur = 1
    x = np.linspace(0, 1, N)
    dx = x[1] - x[0]
    
    u = np.zeros(N+1)
    u[0] = ul
    u[-1] = ur

    a   = np.ones(N)
    b   = np.zeros(N)
    c   = np.zeros(N)
    f   = np.zeros(N)

    for i in range(1, N):
        b[i] = (2 / x[i])
        c[i] = -(2 * p / x[i])

    A = np.zeros((N, N))
    A[0][0] = 1
    A[-1][-1] = 1
    
    B = np.zeros(N)
    B[0] = ul
    B[-1] = ur
    
    f = np.zeros(N)
    
    for i in range(1, N-1):
        A[i][i-1] = a[i] - (b[i]*dx/2)
        A[i][i] = -2*a[i] + c[i]*dx**2
        A[i][i+1] = a[i] + (b[i]*dx/2)
        B[i] = f[i]*dx**2

    return x, gauss_elim(A, B)

x1, u1 = solve(100, 10)
x2, u2 = solve(100, 20)
x3, u3 = solve(100, 50)
x4, u4 = solve(100, 100)
plt.plot(x1, u1, label = "p = 10")
plt.plot(x2, u2, label = "p = 20")
plt.plot(x3, u3, label = "p = 50")
plt.plot(x4, u4, label = "p = 100")
plt.legend()
plt.show()