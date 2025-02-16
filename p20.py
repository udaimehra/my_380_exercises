a = [4, 3, 4.5, 5]
gm = 1
product = 1
inc = 0
for element in a:
    inc = inc + 1
    product = float(element)*product
    print(element, product, inc)
#reciprocal=1/inc
gm = product**(1/inc)
print(f'Geometric average of the given numbers: {gm:.2f}')
