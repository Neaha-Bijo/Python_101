#calculate area and perimeter of triangle
a=float(input('enter lenght of side a= '))
b=float(input('enter lenght of side b= '))
c=float(input('enter lenght of side c= '))
s=(a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))**(1/2)
p=a+b+c
print('perimeter= ', p)
print('area= ', a)