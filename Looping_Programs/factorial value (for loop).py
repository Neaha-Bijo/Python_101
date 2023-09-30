#calculate and output the factorial value
n=int(input('enter value= '))
f=1
for i in range(1,n+1):
    f=f*i             #f*=i
print('factorial= ',f)