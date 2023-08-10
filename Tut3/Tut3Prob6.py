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

A = np.array([[1., 1., 5., 6], [0., 1., 3., 3], [-1., 4., 5, 0.], [2., 3., 0.,4.]])
b0 = np.array([1,0,0,0])
b1 = np.array([0,1,0,0])
b2 = np.array([0,0,1,0])
b3 = np.array([0,0,0,1])

x0 = gauss_elim(A, b0)
x1 = gauss_elim(A, b1)
x2 = gauss_elim(A, b2)
x3 = gauss_elim(A, b3)

B = np.hstack((x0.reshape(4,1), x1.reshape(4,1), x2.reshape(4,1), x3.reshape(4,1)))
print ("B =", B)
# print (np.matmul(A, B))
print (np.allclose(np.matmul(A, B), np.identity(4)))