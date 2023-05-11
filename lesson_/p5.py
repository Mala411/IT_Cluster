x=int(input('1 chislo '))
y=int(input('2 chislo '))
z=int(input('3 chislo '))
for i in range(1, z+1):
    if i % x == 0 and i % y == 0:
        print("FB", end=' ')
    elif i % x == 0:
        print("F", end=' ')
    elif i % 5 == 0:
        print("B", end=' ')
    else:
        print(i, end=' ')
