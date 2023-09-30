l=[]
n=int(input('Enter no of elements:'))
for i in range (n):
    e=int(input('Enter value:'))
    l.append(e)
print(l)
v=int(input('Enter value to search:'))
if v in l:
    c=l.count(v)
    if c==1:
        print(v,'is FOUND',c,'time')
    else:
        print(v,'is FOUND',c,'times')        
else:
    print(v,'is NOT FOUND')
for i in range(len(l)+1):
    if l.index(v,i)==i:
        ind=l.index(v,i)
        print('Index of value:',ind)
    else:
        continue
    
        
