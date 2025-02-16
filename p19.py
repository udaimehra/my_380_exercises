import math
a = 1
b = 5
c = 4
delta = b**2 - 4*a*c
delta_sqrt = math.sqrt(delta)
x1 = (-b-delta_sqrt) / 2*a
x2 = (-b+delta_sqrt) / 2*a
print(f'x1 = {x1:.1f}\nx2 = {x2:.1f}')
