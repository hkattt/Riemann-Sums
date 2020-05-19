# Calculates Riemann Sums

# importing modules
import math

# interval
b = 6
a = 0
# number of subintervals
n = 3
deltaX = (b - a) / n

def f(x):
    return (1 / 3) * math.pow(math.e, ((1 / 3) * x))

def lower_rectangle_method(a, b, n):
    """ Uses the lower rectangle method to approximate area """
    addition_count = 0 # keeps track of the number of additions
    x = 0 # input
    while addition_count < n:
        # adding the area of the rectangle to the total area a
        a += f(x) * deltaX
        # increment x
        x += deltaX
        addition_count += 1
    return a

def upper_rectangle_method(a, b, n):
    """ Uses the upper rectangle method to approximate area """
    addition_count = 0
    x = deltaX # input
    while addition_count < n:
        # adding the area of the rectangle to the total area (a)
        a += f(x) * deltaX
        # increment x
        x += deltaX
        addition_count += 1
    return a

def centered_rectangle_method(a, b, n):
    """ Uses the centered rectangle method to approximate area """
    addition_count = 0
    x = deltaX / 2 # input
    while addition_count < n:
        # adding the area of the rectangle to the total area (a)
        a += f(x) * deltaX
        # increment x
        x += deltaX
        addition_count += 1
    return a

def trapezoid_method(a, b, n):
    """ Uses the trapezoid method to approximate area """
    addition_count = 0
    x = 0
    while addition_count < n:
        # adding the area of the trapezium to the total area (a)
        a += (deltaX / 2) * ((f(x) + f(x + deltaX)))
        # increment x
        x += deltaX
        addition_count += 1
    return a

print("LOWER METHOD:")
print(lower_rectangle_method(a, b, n))
print("")
print("UPPER METHOD:")
print(upper_rectangle_method(a, b, n))
print("")
print("CENTERED METHOD:")
print(centered_rectangle_method(a, b, n))
print("")
print("TRAPEZOID METHOD:")
print(trapezoid_method(a, b, n))