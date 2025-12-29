def factorial(n):
    #base case
    if n==0:
        return 1
    #recursion
    ans = n*factorial(n-1)
    return ans

n= int(input("Enter n: "))
print(factorial(n))
