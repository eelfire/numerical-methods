import numpy as np

def f(vecx):
    x = vecx[0]
    return np.array([x**3 - 1])

def df(vecx):
    x = vecx[0]
    return np.array([[3*x**2]])

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

xa = np.array([0.5j])
xb = np.array([1+1j])
xc = np.array([-2j])
tol = 1e-6
Xa = Newton(xa, tol, f, df)
xb = Newton(xb, tol, f, df)
xc = Newton(xc, tol, f, df)
print(f"x = {Xa}, f(x) = {f(Xa)}")
print(f"x = {xb}, f(x) = {f(xb)}")
print(f"x = {xc}, f(x) = {f(xc)}")
