t1=()
n=int(input('Enter no of elements:'))
for i in range (n):
    e=int(input('Enter value:'))
    t1+=(e,)
print(t1)
t2=()
for i in range (len(t1)):
    if t1[i]<0:
        t2+=(t1[i],)
for i in range (len(t1)):
    if t1[i]>0:
        t2+=(t1[i],)
print(t2)