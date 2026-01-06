#how do you check if a string is a plindrome?

'''def paliindrome(s):
    return s == s[::-1]'''
num= int(input('enter number'))

if num<0 or (num%10 ==0 and num !=0):
    print(False)
else:
    original=num
    rev =0

    while num >0:
        rev = rev*10+num%10
        num//=10

    print(original==rev)
