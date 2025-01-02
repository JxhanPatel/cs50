a = input(print('write an problem')).lower().strip()

x, y, z = a.split(' ')
b = float(x)
c = float(z)

if y =='+':
    print (b + c)

elif y =='*':
    print (b * c)

elif y =='-':
    print (b - c)

elif y =='/':
    print (b / c)

else:
    print ("oops")
