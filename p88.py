items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
final = []
for i in range(0,len(items)):
    if items[i]%2 == 0:
        final.append(items[i])
print(final)
