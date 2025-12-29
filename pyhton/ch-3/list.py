fruits = ["cherry", "lichi", "peach", "mango"] #ceate list
print(fruits)
# print(type(fruits)) #check type of list
# print(len(fruits)) #check length of list
# #checking if an items is present in the list
# if "cherry" in fruits:
#     print("cherry is meri")
# if "kiwi" is not fruits:
#     print("kiwi is not part of list")

# #indexing in list
# print(fruits[2])
# print(fruits[-3])
# print(fruits[1:3])
# print(fruits[-4:-1])


#adding elements to a list
# fruits.append("kiwi")
# print(fruits)

# fruits.insert(2, "kiwi")
# print(fruits)

# more_fruits = ["grapes", "papaya"]
# fruits.extend(more_fruits)
# print(fruits)

#removing elements from aa list
# fruits.remove("mango")
# print(fruits)

# fruits.pop()
# print(fruits)

#changing/ updating items in a list
# fruits[1] = "kiwi"
# print(fruits)

# fruits[1:3] = ["papaya"]
# print(fruits)

#sorting a list
#fruits.sort() #by default ascending order
#fruits.sort(reverse=True) #descending
#print(fruits)

# fruits.reverse()
# print(fruits)

#list comprehension
# new_fruits = [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)


#copy a list
# new_fruits = fruits.copy()
# print(new_fruits)

# new_fruits = fruits + new_fruits
# print(new_fruits)

#nested list
fruits.insert(2, ["kiwi", "papaya"])
print(fruits)
print(fruits[2][0])