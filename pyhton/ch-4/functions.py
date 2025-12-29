#writing a function for calculating sum from 1 to n

def sumToN(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

n = int(input("Enter n: "))
#call function
output = sumToN(n)
print("Sum of all numbers till n is", output)

n1= int(input("Enter n: "))
output2 = sumToN(n1)
print("Sum of all numbers till n is", output2)