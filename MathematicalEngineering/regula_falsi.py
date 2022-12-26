max_iterations = 10_000

def function(x):
    return x**3-x**2+2

a = -100
b = 200

def regula_falsi(a, b):
    if (function(a) * function(b) >= 0):
        print("a i b ne se tocno pretpostaveni")
    return 1

c = a

for iteration in range(max_iterations):
    c= (a * function(b) - (b * function(a))) / (function(b) - function(a))

    if (function(c) == 0):
        break
    elif(function(a) * function(c) < 0):
        b = c
    else:
        a = c
print("resenieto e:", c)
regula_falsi(a, b)