text = 'Python programming'
t1=text.lower().replace(' ', '')
t2=list(set(t1))
t3 = []
for i in t2:
    t3.append(i)
t3.sort()
print(t3)
