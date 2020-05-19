# Calculates Riemann Sums

# importing modules
import math

# interval
b = 6
a = 0
# number of subintervals
n = 3
deltaX = (b - a) / n

def lower_rectangle_method(a, b, n):
    """ Uses the lower rectangle method to approximate area """
    addition_count = 0 # keeps track of the number of additions
    x = 0 # input
    while addition_count < n:
        # adding the area of the rectangle to the total area a
        a += (1 / 3) * math.pow(math.e, ((1 / 3) * x)) * deltaX
        # increment x
        x += deltaX
        addition_count += 1
    return a

def upper_rectangle_method(a, b, n):
    """ Uses the upper rectangle method to approximate area """
    addition_count = 0
    x = deltaX # input
    while addition_count < n:
        # adding the area of the rectangle to the total area a
        a += (1 / 3) * math.pow(math.e, ((1 / 3) * x)) * deltaX
        x += deltaX
        addition_count += 1
    return a

print(upper_rectangle_method(a, b, n))
print(lower_rectangle_method(a, b, n))