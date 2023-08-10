import numpy as np

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

def gauss_seidel(A, b):
    n = len(b)
    error = 10
    tolerance = 1e-6
    iter = 0
    max_iter = 1000
    while error > tolerance and iter < max_iter:
        error = 0
        for i in range(0, n):
            old = x[i]
            x[i] = b[i]
            for j in range(0, n):
                if i != j:
                    x[i] = x[i] - A[i][j]*x[j]
            x[i] = x[i]/A[i][i]
            error = max(error, np.abs((x[i] - old)/x[i]))
    return x

A = np.array([[2.,-6.,-1.],[-3., -1., 7.],[-8., 1., -2.]])
b = np.array([-38., -34., -20.])

x = gauss_elim(A, b)
y = gauss_seidel(A, b)
print ("Gauss Elimination Method, x =", x)
print ("Gauss Seidel Method, x =", y)
#-- Check that the solution satisfies the equation
print (np.allclose(np.matmul(A, x), b))
print (np.allclose(np.matmul(A, y), b))