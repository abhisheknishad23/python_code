#a combination of numbers and stars

row = 4
for i in range(0, row):
    c=1
    print(c, end=' ')
    for j in range(row - i - 1, 0, -1):
        print('*', end=' ')
        c=c+1
        print(c, end=' ')
    print('\n')