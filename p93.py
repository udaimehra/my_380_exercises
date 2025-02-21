items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
s = list(set(items))
d = {}
for item in s:
    d[item] = items.count(item)
print(d)
