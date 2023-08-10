# Develop a program to solve set 0f 2n non linear equations using Newton's method.

import numpy as np

def f(x, c, k):
    f = np.zeros(2*k)
    for i in range(0, 2*k):
        sum = 0
        for j in range(0, k):
            sum += (x[j]**(i-1))*c[j]
        f[i] = sum - (1 - (-1)**i)/k

    return f

def df(x, c, k):
    df = np.zeros((2*k, 2*k))
    for i in range(0, 2*k):
        for j in range(0, k):
            df[i][j] = (i-1)*(x[j]**(i-2))*c[j]
    return df

def newton(x, c, k):
    for i in range(0, 100):
        x = x - np.linalg.inv(df(x, c, k)).dot(f(x, c, k))
    return x

def solve(c, k):
    x = np.zeros(k)
    for i in range(0, k):
        x[i] = 1
    x = newton(x, c, k)
    return x

def main():
    c = np.array([1, 2, 3, 4, 5])
    k = len(c)
    x = solve(c, k)
    print(x)

if __name__ == "__main__":
    main()
