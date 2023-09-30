n=int(input('enter number:'))
f=0
i=1
while i<=n:
    if n%i==0:
        f+=1
    i+=1    
if f<=2:
    print('prime')
else:
    print('composite')