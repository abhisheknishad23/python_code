#for converting characters to uppercase
str1 = "new york"
str2 = str1.upper()
print(str2)

# #for converting character to lowercase
str3 = str2.lower()
print(str3)

#for capitalising the first character of my string
str4 = str3.capitalize()
print(str4)

#for stripping/removing any trailing whitespaces
str1 = "   hello world!  "
print(str1.strip())
print(str1)

#replacing substring
str1 = "Hello world, what a beautiful world this is"
print(str1.replace("world", "earth",1))

#spilitting string
str1 = "ak,bk,ck,dk"
list = str1.split(",", 2)
print(list)

#concatenation
str1 = "Hello World"
str2 = "what a great place this is."
print(str1 + str2)

#string formatting
stu_name = "abhishek"
stu_marks = 96
str1 = "The student name is {s}, and marks is {m}".format(s=stu_name, m=stu_marks)
print(str1)

text = "The unexpected alwayes happens "
print(text)
print(len(text))
print(text.find('T'))
print(text[:11])
print(text.replace('alwayes','never'))
text2 = "no matter what"
new_text = text + text2
print(new_text)