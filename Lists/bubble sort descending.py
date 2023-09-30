l=[313,901,116,220,16,77]
n=len(l)
for j in range(n-1):
    for i in range(n-j-1):
        if l[i]<l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    print('Pass',j+1,':',l)   