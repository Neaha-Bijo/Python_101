l=['490','913','20','@','66','2527','7759']
for i in l:
    j=0
    for n in i:
        if n.isdigit():
            j=j+1
    print('value',i,':',j,'digits')
    