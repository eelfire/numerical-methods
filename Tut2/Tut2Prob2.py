import numpy as np

def f(x):
    return np.exp(x) - x - 1

def df(x):
    return np.exp(x) - 1

def newton_method(x0, tol=1e-8, maxiter=100):
    for i in range(maxiter):
        fx = f(x0)
        # if np.allclose(fx,np.array([0,0]),rtol=tol):
        if np.linalg.norm(fx) < tol:
            print(f"Converged in {i+1} iterations.")
            return x0
        else:
            dfx = df(x0)
            dx = fx/dfx
            x0 = x0-dx

    print(" Did not converge")
    return None

x0 = 1
x = newton_method(x0)
print(x, f(x))