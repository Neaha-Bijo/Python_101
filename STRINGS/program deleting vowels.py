s = input("Enter any string: ")
ns = s
v = ['a', 'e', 'i', 'o', 'u']
for x in s:
    if x in v:
        ns = ns.replace(x,"")
print(ns)
    
 


