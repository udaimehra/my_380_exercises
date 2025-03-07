pv = 1000
r = 0.04
n = 0
while pv < 2000:
    pv = pv*1.04
    n = n + 1
print(f'Future value: {pv:.2f} USD. Number of periods: {n} years')
