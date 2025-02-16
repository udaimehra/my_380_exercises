import math
a = [10, 11, 9]
n = len(a)
m = float(sum(a)/n)
print(n, m)
b = ((a[0]-m)**2 + (a[1]-m)**2 + (a[2]-m)**2)/n
b = math.sqrt(b)
print(f'The standard deviation: {b:.2f}')
