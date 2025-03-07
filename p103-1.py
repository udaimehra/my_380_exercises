counter = 0
number = 2
prime = []
while counter <10:
    for i in range(2, number):
        if number%i == 0:
            break
    else:
            prime.append(str(number))
            counter = counter + 1
    number = number + 1
print(','.join(prime))  
