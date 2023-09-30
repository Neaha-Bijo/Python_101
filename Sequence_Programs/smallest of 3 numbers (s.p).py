# smaillest of three numbers
n1=float(input('enter number n1= '))
n2=float(input('enter number n2= '))
n3=float(input('enter number n3= '))
if n1<n2:
    if n1<n3:
        print('smallest number= ',n1)
    else:
        print('smallest number= ',n3)
elif n2<n3:
    print('smallest number= ',n2)
else:
    print('smallest number= ',n3)
    