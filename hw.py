from fraction import *

points = [
    (8, -4),
    (6, 0),
    (17/2, -5),
    (0, 0),
    (9, -9/2),
    (0, -5),
    (9, -5),
    (9, 0)
]

def T(x, y):
    return x**2 + x*y + y**2 - 12*x +8

for point in points:
    print(f"{point} : {formatted_fraction(T(point[0], point[1]))} = {T(point[0], point[1])}")
