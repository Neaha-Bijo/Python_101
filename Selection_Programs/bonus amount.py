#bonus calculation
n = int(input('enter no. extra hours : '))
if n >= 1 and n <= 8:
    b = n * 25
elif n >= 9 and n <= 15:
    b = (8 * 25)  + (n - 8)*50
elif n >= 16 and n <= 20:
    b = (8 * 25) + (7 * 50) +(n - 15)*75
elif n > 20:
    b = (8 * 25) + (7 * 50) + (5 * 75) +(n - 20)*100
print('bonus amount :  ',b)
