#write a python function to check if a number is prime

n=int(input('Enter a number'))

if n <=1:
    print('not prime')
else:
    for i in range(2, int(n**0.5)+1):
        if n %i ==0:
            print('Not prime')
            break
    else:
        print("Prime number")