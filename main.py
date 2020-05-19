# Calculates Riemann Sums

# importing modules
import math

# interval
b = 6
a = 0
# number of subintervals
n = 3
# calculates the rectangles width
deltaX = (b - a) / n

def f(x):
    """ acts like a mathematical function """
    return (1 / 3) * math.pow(math.e, ((1 / 3) * x))

def lower_rectangle_method(a, b, n):
    """ Uses the lower rectangle method to approximate area """
    x = 0 # input
    for _ in range(n):
        # adding the area of the rectangle to the total area a
        a += f(x) * deltaX
        # increment x
        x += deltaX
    return a

def upper_rectangle_method(a, b, n):
    """ Uses the upper rectangle method to approximate area """
    x = deltaX # input
    for _ in range(n):        # adding the area of the rectangle to the total area (a)
        a += f(x) * deltaX
        # increment x
        x += deltaX
    return a

def centered_rectangle_method(a, b, n):
    """ Uses the centered rectangle method to approximate area """
    x = deltaX / 2 # input
    for _ in range(n):        # adding the area of the rectangle to the total area (a)
        a += f(x) * deltaX
        # increment x
        x += deltaX
    return a

def trapezoid_method(a, b, n):
    """ Uses the trapezoid method to approximate area """
    x = 0
    for _ in range(n):        # adding the area of the trapezium to the total area (a)
        a += (deltaX / 2) * ((f(x) + f(x + deltaX)))
        # increment x
        x += deltaX
    return a

print("LOWER METHOD:")
print(str(lower_rectangle_method(a, b, n)) + " units squared")
print("")
print("UPPER METHOD:")
print(str(upper_rectangle_method(a, b, n)) + " units squared")
print("")
print("CENTERED METHOD:")
print(str(centered_rectangle_method(a, b, n)) + " units squared")
print("")
print("TRAPEZOID METHOD:")
print(str(trapezoid_method(a, b, n)) + " units squared")
print("")