string = '1 0 0 1 0 1'
str=string[::2]
m = 2
s = int(0)
n = int(len(str))
for i in str:
    n = n - 1
    i = int(i)
    s = s+((i)*(2**n))
print('Number found:', s)
