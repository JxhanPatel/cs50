cc = input('Thy camelCase? : ')
print('My snake_case is : ', end="")

for a in cc:
    if a.islower():
        print(a, end='')
    elif a.isupper():
        print ('_', a.lower(), end='', sep='')

print()
