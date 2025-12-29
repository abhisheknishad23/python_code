#write a python function that checks if the given string is a palindrome or not.



def check_palindrome(str):

    #cleaning the str
    clean_str = (str.replace(" ", "")).lower()

    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str = input("Enter a string: ")
if check_palindrome(str):
    print("It is a palindrome string")
else:
    print("Not a palindrome")