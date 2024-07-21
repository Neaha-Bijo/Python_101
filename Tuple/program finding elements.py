t=()
n=int(input('Enter no of elements:'))
for i in range (n):
    e=int(input('Enter value:'))
    t+=(e,)
print(t)
v=int(input('Enter value to search:'))
if v in t:
    print(v,'is FOUND at location',t.index(v)+1)
else:
    print(v,'is NOT FOUND')
