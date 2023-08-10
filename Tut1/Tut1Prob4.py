### Tut 1 Prob 4: Solve H in manning equation using fixed point iteration

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

Q = 5
S = 0.0002
B = 20
n = 0.03

def H(H):
    return (Q*n/(S**(1/2)))**(3/5)*(B+2*H)**(2/5)/B

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
    x_prev = 1
    initial_error = 10
    tolerance = 1e-6
    H = fixed_point_iteration(x_prev, initial_error, tolerance, H)
    print("H =", H)
