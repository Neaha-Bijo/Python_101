n=int(input('enter n:'))
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print('sum of digits:',s)