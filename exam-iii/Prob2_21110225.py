import numpy as np
import matplotlib.pyplot as plt

# d^2u/dx^2 = Lamda * sinh(u)

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

def solve(N, Lamda):
    ul = 2
    ur = 2
    xl = 0
    xr = 1
    x = np.linspace(xl, xr, N)
    dx = x[1] - x[0]
    
    u = np.zeros(N+1)
    u[0] = ul
    u[-1] = ur

    f   = np.zeros(N)

    A = np.zeros((N, N))
    A[0][0] = 1
    A[-1][-1] = 1

    B = np.zeros(N)
    B[0] = ul
    B[-1] = ur

    f = np.zeros(N)
    M = np.zeros((N, N))
    for i in range(1, N-1):
        for j in range(1, N-1):
            M[i][j] = np.cosh(u[i])

    for i in range(1, N-1):
        if i%2 == 0:
            f[i] = Lamda * M[i][i] * np.sinh(u[i])
        else:
            f[i] = Lamda * M[i][i] * np.cosh(u[i])

    for i in range(1, N-1):
        A[i][i] = -2
        A[i][i-1] = 1 - (dx**2)*Lamda
        A[i][i+1] = 1
        B[i] = -f[i]*(dx**2)

    return x, gauss_elim(A, B)

x, u = solve(50, 25)
plt.plot(x, u)
plt.show()