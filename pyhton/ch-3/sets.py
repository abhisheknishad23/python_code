#creating a set
names = {"abhishek", "alok", "sidharth"}
print(names)

#check length of sets
print(len(names))

#check data type of sets
print(type(names))

#accessing items in sets
for x in names:
    print(x)

#check if an item exists in a set
if "abhishek" in names:
    print("abhisek is in a set")

#add elements in set
#names.add()

#add another sequence in a set
names_list = ["ria", "khushi"]
names.update(names_list)
print(names)

#removing elements from set
names.remove("alok")
names.discard("mia") #this function will not throw an error if values is not present in sets
print(names)

#joining 2 sets
s1 = {"a","b"}
s2 = {"c", "d", "a"}
s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

#keep only duplicates while joining
s1.intersection_update(s2)
print(s1)

#keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)