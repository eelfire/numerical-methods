import numpy as np

def f(x):
    f1 = x[0]**2 - x[1] + x[2]**3
    f2 = x[0]*x[1] - x[2]**2 - 1
    f3 = (x[0]**2) * (x[2]**2) - x[1] + 1
    return np.array([f1, f2, f3])


def df(x):
    J = np.array([
        [2*x[0], -1, 3*x[2]**2],
        [x[1], x[0], -2*x[2]],
        [2*x[0]*x[2]**2, 2*x[2]*x[0]**2, -1]
    ])
    return J


def newton_method(x, tol=1e-8, maxiter=100):
    for i in range(maxiter):
        fx = f(x)
        # if np.allclose(fx,np.array([0,0]),rtol=tol):
        if np.linalg.norm(fx) < tol:
            print(f"Converged in {i+1} iterations.")
            return x
        else:
            dfx = df(x)
            dx = np.linalg.solve(dfx, -fx)
            x = x+dx

    print(" Did not converge")
    return None


x0 = [1000, 1000, 1000]
x = newton_method(x0)
print(x, f(x))