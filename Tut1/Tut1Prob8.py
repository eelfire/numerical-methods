### Tut 1 Prob 8: modified secant method for f(x) = 0

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

def f(x):
    return x**5 + 16.05*x**4 + 88.75*x**3 - 132.0375*x**2 + 116.35*x + 31.6875

# modified secant method
def modified_secant_method(x_prev, del_x, initial_error, tolerance, f):
    error = initial_error
    count = 0
    max_iter = 1000
    while error > tolerance:
        x = x_prev - f(x_prev)*del_x/(f(x_prev + del_x) - f(x_prev))
        error = Error(x, x_prev)
        x_prev = x
        count += 1
        if count > max_iter:
            return f"{x} | Max iterations reached."
    return x

if __name__ == "__main__":
    x0 = 0.5825
    del_x = 0.05
    initial_error = 10
    tolerance = 1e-6
    x = modified_secant_method(x0, del_x, initial_error, tolerance, f)
    print("x = ", x)
