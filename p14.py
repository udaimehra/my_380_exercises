#Nth value of a can be derived using 10 + 4n
#Calculate the sum of the first ten elements of this sequence.
# Print the result to the console as shown below.
sum = 0
for i in range(11):
    if i > 0:
        sum = sum + 10+(4*i)
print(f'The sum of the first 10 elements in a sequence: {sum:.1f}')
