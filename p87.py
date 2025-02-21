n = 100
arr = []
for i in range(1,n):
    if ( i%11 == 0 and i%3 != 0 and len(str(i)) != 1 ):
        arr.append(str(i))
arr_str = ','.join(arr)
print(arr_str)


