t=()
n=int(input('Enter no of elements:'))
for i in range (n):
    e=int(input('Enter value:'))
    t+=(e,)
print(t)
s=sum(t)
avg=s/n
print('Sum of all numbers:',s)
print('Average of all numbers:',avg)