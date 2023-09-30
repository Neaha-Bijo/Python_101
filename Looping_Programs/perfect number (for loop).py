n=int(input('enter number:'))
f=0
for i in range(1,n):
    if n%i==0:
        f+=i
if f==n:
    print('perfect number')
else:
    print('not a perfect number')