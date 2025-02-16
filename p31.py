text = 'python is a popular programming language.'
char = 'p'
sum = 0
for i in text:
    if i == char:
        sum = sum + 1
print(f'Number of occurrences: {sum:.0f}')
