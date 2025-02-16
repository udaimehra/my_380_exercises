#The geometric sequenc is given with the following formula:
# nth value of a = an= 8.2^(n-1)
#valculae the sum of hte first six elements of this sequence. Print the result to the console as shown below.
n=6
i=1
sum=0
while i<=n:
    sum=sum+(8*(2**(i-1)))
    i = i+1
    print(sum)

print(f'The sum of the first {n:} elements of the sequence is: {sum:.1f}')
