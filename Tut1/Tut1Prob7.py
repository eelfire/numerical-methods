### Tut 1 Prob 7: Secant method for f(x) = 0

import numpy as np

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

def f(x):
    return 7*np.sin(x)*np.exp(-x) - 1

# secant method
def secant_method(x_prev, x_prev_prev, initial_error, tolerance, f):
    error = initial_error
    count = 0
    max_iter = 1000
    while error > tolerance:
        x = x_prev - f(x_prev)*(x_prev - x_prev_prev)/(f(x_prev) - f(x_prev_prev))
        error = Error(x, x_prev)
        x_prev_prev = x_prev
        x_prev = x
        count += 1
        if count > max_iter:
            return f"{x} | Max iterations reached."
    return x

if __name__ == "__main__":
    x0 = 0.5
    x00 = 0.4
    initial_error = 1
    tolerance = 1e-6
    x = secant_method(x0, x00, initial_error, tolerance, f)
    print("x = ", x)
    