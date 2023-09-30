# discount of tv
ba=float(input('enter bill amount= '))
if ba>=9000:
    d=(40*ba)/100
elif ba>=7500 and ba<=8999:
    d=(30*ba)/100
elif ba<=7499:
    d=(20*ba)/100
else:
    print('invalid')
    
print('discount= ',d)