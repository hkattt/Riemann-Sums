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
    x = a # input
    # area
    A = 0
    for _ in range(0, n):
        # adding the area of the rectangle to the total area (A)
        A += f(x) * deltaX
        # increment x
        x += deltaX
    return A

def upper_rectangle_method(a, b, n):
    """ Uses the upper rectangle method to approximate area """
    x = a + deltaX # input
    # area
    A = 0
    for _ in range(0, n):        
        # adding the area of the rectangle to the total area (A)
        A += f(x) * deltaX
        # increment x
        x += deltaX
    return A

def centered_rectangle_method(a, b, n):
    """ Uses the centered rectangle method to approximate area """
    x = a + (deltaX / 2) # input
    # area
    A = 0
    for _ in range(0, n):        
        # adding the area of the rectangle to the total area (A)
        A += f(x) * deltaX
        # increment x
        x += deltaX
    return A

def trapezoid_method(a, b, n):
    """ Uses the trapezoid method to approximate area """
    x = a
    # area
    A = 0
    for _ in range(0, n):        
        # adding the area of the trapezium to the total area (A)
        A += (deltaX / 2) * ((f(x) + f(x + deltaX)))
        # increment x
        x += deltaX
    return A

print("LOWER METHOD:")
print(str(lower_rectangle_method(a, b, n)) + " units squared")
#print("ERROR")
#print((math.pow(math.e, 2) - 1) - lower_rectangle_method(a, b, n))

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
