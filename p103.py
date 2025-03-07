max_prime_count = 10
max_number = 50
number = 4
begin = 2
prime = ['2', '3']
while len(prime) < 10:
    #print("number is", number)
    for i in range(begin, (number//2)+1):
        #print("divisor is", i)
        if number%i != 0:
            max_prime_count = max_prime_count + 1
            is_prime = True
        else:
            #print(f'{number} is divisible by {i}')
            is_prime = False
            break;
    if is_prime == True:
        #print(f'{number} ---- is a prime number')
        prime.append(str(number))
    number = number + 1
prime_string = ','.join(prime)
print(prime_string)
