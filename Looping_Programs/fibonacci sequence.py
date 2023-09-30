n=int(input('enter number: '))
fn=0      #first number
sn=1      #second number
if n==1:
    print(fn)
elif n==2:
    print(fn,sn)
else:
    print(fn,sn,'',end='')
    for i in range (0,n):
        tn=fn+sn   #third number
        print(tn,'',end='')
        fn=sn
        sn=tn