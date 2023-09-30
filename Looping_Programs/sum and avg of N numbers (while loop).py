n=int(input('enter no. of number= '))
s=0
i=1
while(i<=n):
    num=int(input('enter a number= '))
    s=s+num
    i=i+1
a=s/float(n)
print('sum= ',s)
print('average= ',a)