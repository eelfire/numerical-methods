### Tut 1 Prob 1: Bisection method for p(v) = 0

def Error(error_current, error_previous):
    if error_current == 0:
        return abs(error_current - error_previous)
    else:
        return abs((error_current - error_previous) / error_current)

R = 518

pc = 4580000 #Pa
tc = 191 #K

T = -50 + 273.15 #K 
p = 65000 #Pa

a = (0.427*(R**2)*(tc**2.5))/pc
b = 0.0866*R*(tc/pc)

# Redlich-Kwong equation of state
def P(v):
    return R*T/(v-b) - a/(v*(v+b)*T**(0.5)) - p

def bisection_method(initial_error, tolerance, vl, vu, f):
    if f(vl)*f(vu) > 0:
        # print("Invalid interval.")
        return "NA | Invalid interval."
    error = initial_error
    v_prev = vl
    while error > tolerance:
        v = (vl + vu)/2
        if f(vl)*f(v) < 0:
            vu = v
        else:
            vl = v
        error = Error(v, v_prev)
        v_prev = v
    return v

if __name__ == "__main__":
    vl = 1
    vu = 5
    initial_error = 10
    tolerance = 1e-6
    v = bisection_method(initial_error, tolerance, vl, vu, P)
    print("v =", v)
    