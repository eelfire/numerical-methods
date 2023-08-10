### Tut 1 Prob 6: Newton's method for f(x) = 0

import math as m

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

def f(x):
    return m.exp(-0.5*x)*(4-x) - 2

def f_prime(x):
    return -0.5*m.exp(-0.5*x)*(4-x) - m.exp(-0.5*x)

# newton's method
def newton_method(x_prev, initial_error, tolerance, f, f_prime):
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
    initial_error = 10
    tolerance = 1e-6
    xa = 2
    xb = 6
    xc = 8
    Xa = newton_method(xa, initial_error, tolerance, f, f_prime)
    Xb = newton_method(xb, initial_error, tolerance, f, f_prime)
    Xc = newton_method(xc, initial_error, tolerance, f, f_prime)
    print("Using x0 = 2: x =", Xa)
    print("Using x0 = 6: x =", Xb)
    print("Using x0 = 8: x =", Xc)