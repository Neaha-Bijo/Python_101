# largest of three numbers
a=float(input('enter number a= '))
b=float(input('enter number b= '))
c=float(input('enter number c= '))
if a>b:
    if a>c:
        print('largest number= ',a)
    else:
        print('largest number c= ',c)
elif b>c:
    print('largest number= ',b)
else:
    print('largest number= ',c)