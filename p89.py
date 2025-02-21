items = [1, 5, 3, 2, 2, 4, 2, 4]
uni = []
for item in items: 
    if not item in uni:
        uni.append(item)
print(uni)
