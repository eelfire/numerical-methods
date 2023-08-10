### Tut 1 Prob 2: Develop a fixed point iteration method for finding the square root of a number

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

def f(x):
    return (number/x + x/2)*2/3

# fixed point iteration method
def fixed_point_iteration(x_prev, initial_error, tolerance, f):
    error = initial_error
    count = 0
    max_iter = 1000
    while error > tolerance:
        x = f(x_prev)
        error = Error(x, x_prev)
        x_prev = x
        count += 1
        if count > max_iter:
            return f"{x} | Max iterations reached."
    return x

if __name__ == "__main__":
    number = 100
    x_prev = 1
    initial_error = 10
    tolerance = 1e-6
    square_root = fixed_point_iteration(x_prev, initial_error, tolerance, f)
    print(f"Square root of {number} =", square_root)
