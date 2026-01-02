#write a python code to count the number of vowels in a string

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("Abhishek"))