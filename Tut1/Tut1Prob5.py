### tut-1-5.py: Locate first positive root of f(x) = 0 using Newton's method

# import utils as ut 
import numpy as np

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

def f(x):
    return np.sin(x) + np.cos(1+x**2) - 1

def f_prime(x):
    return np.cos(x) - 2*x*np.sin(1+x**2)

def newton_method(x_prev, initial_error, tolerance):
    error = initial_error
    count = 0
    max_iter = 1000
    while error > tolerance:
        if f_prime(x_prev) == 0:
            return f"NA | f'({x_prev}) = 0. Solution not found."
        x = x_prev - f(x_prev)/f_prime(x_prev)
        error = Error(x, x_prev)
        x_prev = x
        count += 1
        if count > max_iter:
            return f"{x} | Max iterations reached."
    return x

if __name__ == "__main__":
    xa = 0.1
    xb = 2
    xc = 0.2
    xd = 1
    initial_error = 10
    tolerance = 1e-6
    fa = newton_method(xa, initial_error, tolerance)
    fb = newton_method(xb, initial_error, tolerance)
    fc = newton_method(xc, initial_error, tolerance)
    fd = newton_method(xd, initial_error, tolerance)
    print("Using x0 = 0.1: x =", fa)
    print("Using x0 = 2.0: x =", fb)
    print("Using x0 = 0.2: x =", fc)
    print("Using x0 = 1.0: x =", fd)