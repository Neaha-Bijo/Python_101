l=[20,67,50,89,45,23]
e=len(l)
for i in range (0,e,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)