opt=0
while opt!=7:
    print('**********MENSURATION MENU***********')
    print()
    print('1-Perimeter of RECTANGLE')
    print('2-Area of RECTANGLE')
    print('3-Circumference of CIRCLE')
    print('4-Area of Circle')
    print('5-Perimeter of SQUARE')
    print('6-Area of SQUARE')
    print('7-EXIT')
    print()
    print('*************************************')
    print()
    opt=int(input('Enter option:'))
    if opt==1:
        l=int(input('Enter length:'))
        b=int(input('Enter breadth:'))
        p=2*(l+b)
        print('Perimeter of RECTANGLE:',p)
    elif opt==2:
        l=int(input('Enter length:'))
        b=int(input('Enter breadth:'))
        a=l*b
        print('Area of RECTANGLE:',a)
    elif opt==3:
        r=int(input('Enter radius:'))
        c=2*22.0/7.0*r
        print('Circumference of CIRCLE:',c)
    elif opt==4:
        r=int(input('Enter radius:'))
        a=22.0/7.0*(r**2)
        print('Area of CIRCLE:',a)
    elif opt==5:
        s=int(input('Enter side length:'))
        p=4*s
        print('Perimeter of SQUARE:',p)
    elif opt==6:
        s=int(input('Enter side length:'))
        a=s*s
        print('Area of SQUARE:',a)
    elif opt==7:
        print('EXIT')
        break
    else:
        print('Wrong Option')
    print()
    
    