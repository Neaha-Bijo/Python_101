l=[313, 116, 220, 16, 901, 77]
n=len(l)
for i in range(1,n):
    t=l[i]
    j=i-1
    while (j>=0) and l[j]<t:
        l[j+1]=l[j]
        j-=1
    l[j+1]=t
    print('pass',i,':',l)