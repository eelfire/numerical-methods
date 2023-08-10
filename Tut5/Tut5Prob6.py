# Given equation after converting into second order BVP:
# d^2psi/dx^2 + (2/r)*dpsi/dx = λ^2 * psi

# Given:
# ψ(r = 1) = 1 and dψ/dr = 0 at r = 5. 

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

def solve(N, Lamda):
    ul = 1
    # ur = 0
    x = np.linspace(1, 5, N)
    dx = x[1] - x[0]

    du_r = 0
    
    u = np.zeros(N+1)
    u[0] = ul
    # u[-1] = ur

    a   = np.ones(N)
    b   = np.zeros(N)
    c   = np.zeros(N)
    f   = np.zeros(N)

    for i in range(1, N):
        b[i] = (2 / x[i])
        c[i] = -(Lamda**2)

    A = np.zeros((N, N))
    A[0][0] = 1
    A[-1][-1] = 1
    
    B = np.zeros(N)
    B[0] = ul
    # B[-1] = ur
    
    f = np.zeros(N)

    A[N-1][N-2] = 2 * a[N - 1]
    A[N-1][N-1] = - (2*a[N - 1] - c[N - 1]*dx**2)
    B[N-1]      = - (du_r)*(2*dx)*(a[N - 1] + b[N - 1]*dx/2)
    # A[N-1][N-1]     = 1
    
    for i in range(1, N-1):
        A[i][i-1] = a[i] - (b[i]*dx/2)
        A[i][i] = -2*a[i] + c[i]*dx**2
        A[i][i+1] = a[i] + (b[i]*dx/2)
        B[i] = f[i]*dx**2

    return x, gauss_elim(A, B)

x1, psi1 = solve(100, 3)
x2, psi2 = solve(100, 4)
x3, psi3 = solve(100, 6)
x4, psi4 = solve(100, 1)
plt.plot(x1, psi1, label="λ = 3")
plt.plot(x2, psi2, label="λ = 4")
plt.plot(x3, psi3, label="λ = 6")
plt.plot(x4, psi4, label="λ = 1")
plt.legend()
plt.show()