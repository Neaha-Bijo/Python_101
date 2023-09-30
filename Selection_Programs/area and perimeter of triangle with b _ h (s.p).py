#area and perimeter of triangle
b=float(input('enter lenght of base= '))
h=float(input('enter lenght of height= '))
ar=0.5*b*h
print('area= ',ar)
hyp=(h**2+b**2)**(1/2)
p=b+h+hyp
print('perimeter=',p)