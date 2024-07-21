t=()
n=int(input('Enter no of elements:'))
for i in range (n):
    e=int(input('Enter value:'))
    t+=(e,)
print(t)
v=int(input('Enter value to search:'))
if v in t:
    c=t.count(v)
    if c==1:
        print(v,'is FOUND',c,'time')
    else:
       print(v,'is FOUND',c,'times')        
else:
    print(v,'is NOT FOUND')