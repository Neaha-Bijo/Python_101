#tax calculation
sa=float(input('enter sales amount= '))
if sa<100:
    t=0
    ta=sa+t
elif sa>=100 and sa<=500:
    t=sa*10/100
    ta=sa+t
elif sa>=500 and sa<=1000:
    t=sa*15/100
    ta=sa+t
else:
    t=sa*25/100
    ta=sa+t
print('tax amount: ',t)
print('total amount: ',ta)