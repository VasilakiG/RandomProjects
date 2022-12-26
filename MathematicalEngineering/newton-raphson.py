import numpy as np
from scipy.misc import derivative

EPSILON = 0.000001

# Our f(x) function
def f(x):
    y = x**2 - 3
    return y
    
# The Newton-Raphson function
def NewtonRaphson(f, xi):
    x = xi
    i = 0
    print("---------------------------------------------")
    while abs(f(x)) > EPSILON:
        fx = f(x)
        dfx = derivative(f, x, EPSILON)
        x = x - (fx/dfx)
        print(f"|  {i}. \t {x} \t|")
        i += 1
    print("---------------------------------------------")
    return x
    
printable = NewtonRaphson(f, 4)
print(f"|      Result is:    {printable}  |")

print("---------------------------------------------")