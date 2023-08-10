import numpy as np

def f(x):
    return np.array([x[0]**2 + x[1]**2 - 16, (x[0] - 4)**2 + (x[1] - 4)**2 - 5])

def df(x):
    return np.array([[2*x[0], 2*x[1]], [2*(x[0] - 4), 2*(x[1] - 4)]])

def Newton(x0, tol, f, df):
    x = x0
    max_iter = 100
    for i in range(max_iter):
        if np.linalg.norm(f(x)) < tol:
            print(f"Converged in {i+1} iterations.")
            return x
        else:
            dx = np.linalg.solve(df(x), -f(x))
            x = x + dx
    print("Did not converge")
    return None

x0 = np.array([30,1.805])
tol = 1e-6
x = Newton(x0, tol, f, df)
print(f"x = {x}, f(x) = {f(x)}")