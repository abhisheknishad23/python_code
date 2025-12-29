#given a string and a number N, we need to mirrir the character from the N-th position up to the length of the string in alphabetical order. in mirror operation, we change 'a' to 'z' 'b' to 'y' and so on

#input: N=3
#paradox
#output: paizwlc

input_string = input("Enter string ")
n = int(input("enter n: "))

#creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reversr_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reversr_alphabets))

#finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string
mirror = "" 
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
res = prefix + mirror
print("the result is ", res)