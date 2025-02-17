A = {2, 4, 6, 8}
B = {4, 10}
C = set()
for i in A:
    if i not in B:
        C.add(i)
for i in B:
    if i not in A:
        C.add(i)
print(f'Symmetric difference: {C}')
