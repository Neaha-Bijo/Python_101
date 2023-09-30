# diScount and net amount
sa=float(input('enter sale amount= '))
if sa>=0 and sa<=100:
    d=(sa*5)/100
elif sa>=101 and sa<=500:
    d=(sa*10)/100
elif sa>=500:
    d=(sa*25)/100
else:
    print('invalid amount')
na=sa-d
print('discount= ',d)
print('net amount= ',na)