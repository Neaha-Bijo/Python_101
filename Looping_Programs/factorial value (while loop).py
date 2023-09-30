#calculate and output the factorial value
n=int(input('enter value= '))
f=1
i=1
while i<=n:
    f=f*i    #f*=i
    i+=1
print('factorial= ',f)