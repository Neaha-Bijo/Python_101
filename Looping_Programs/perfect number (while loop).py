n=int(input('enter number:'))
f=0
i=1
while i<n:
    if n%i==0:
        f+=i
    i+=1
if f==n:
    print('perfect number')
else:
    print('not a perfect number')