l=[]
n=int(input('Enter the no. of numbers to be added='))
for i in range (n):
    v=float(input('Enter value to be added='))  #v=value 
    l.append(v)
print(l)
l2=[]
cs=0  #cs=cumulative sum
for i in range(n):
    cs+= l[i]
    l2.append(cs)
print(l2)