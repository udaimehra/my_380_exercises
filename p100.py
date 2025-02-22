number = 13
for i in range(2, (number//2)+1):
    if (number%i) != 0:
        print(f'{number} - prime number')
        break;
