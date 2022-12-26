import numpy as np
from scipy.misc import derivative
import sys

a = 1
b = 2
epsilon = 0.000001

x = a

def f(x):
    y = x**2 - 2
    return y

fx = f(x)
dfx = derivative(f, x, epsilon)
ddfx = derivative(f, x, epsilon, 2)

# print(f"dfx e {dfx}, a ddfx e {ddfx}")

if fx*ddfx < 0:
    x = b
    y = x - (fx / dfx)

while (abs(x - y)) > epsilon:
    x = y
    dfx = derivative(f, x, epsilon)
    y = x - (fx / dfx)
    print(y)

print(f"Resenieto e {x}")