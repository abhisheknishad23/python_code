try:
    num  = int(input('enter a number'))
    result = 10/num
    print(f'result: {result}')

except ZeroDivisionError:
    print('you can not divide with 0')

except ValueError:
    print('you can not divide with string')