item = '001'
items = ['001', '000', '003', '005', '006']
for i in range(0,len(items)):
    if items[i] == item:
        pos = int(i)
items.pop(pos)
print(items)
