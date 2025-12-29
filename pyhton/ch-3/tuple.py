#creating a tuple
colours = ("green", "red", "blue")

#creating a tuple with 1 item
fruit = ("lichi",)

#check type of tuple
print(type(fruit))
print(type(colours))

#check length of tuple
print(len(colours))

#accessing items in tuple
print(colours[1]) #positive indexing
print(colours[-1]) #negative indexing
print(colours[1:3]) #range indexing
print(colours[-2:]) #negative range

#check if an item exists in tuple
if "green" in colours:
    print("green is part of tuple")

#traverse the tuple
for i in colours:
    print(i)

#concatenate 2 tuple
more_colours = ("blue", "brown")
colours = colours + more_colours
print(colours)

#unpacking a tuple
# colour1, colour2, colour3 = colours
# print(colour1, colour2, colour3)
