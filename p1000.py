str=input('Input the string: ')
pos = []
for i in str:
    if i.isupper():
        pos.append((str.index(i)))
print(pos)
