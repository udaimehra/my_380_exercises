n = int(100)
eleven = []
for i in range(1,n+1):
    i = i + 1
    if i%11 == 0:
        #print(f'{i} is divisible by 11')
        eleven.append(str(i))
str_eleven = ','.join(eleven)
print(str_eleven)
