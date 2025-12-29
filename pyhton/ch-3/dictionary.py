#creating dictionary
number = {
    "abhishek":48484848,
    "Hiba": 484541544,
    "sid" : 545582552
}
print(number)
#check type od dict
print(type(number))

#check the lenth of dict
print(len(number))

#access item of dict
print(number["abhishek"])
print(number.get("Hiba"))
print(number.keys())

#update value in dict
number["abhishek"]= 7992035702
print(number)

#add elements in dict
number["alok"] = 888585858
print(number) 

more_number = {
    "zoya" : 87878\
}
number.update(more_number)
print(number)

#remove elements in a dict
number.pop("zoya")
print(number)

number.popitem() #this will remove the last added item
print(number)

# number.clear() #this will empty the dict
# print(number)

#printing values of a dict
for x,y in number.items():
    print(x,y)

#nested dictionary

number = {
    "area1":{
        "a": 1,
        "b": 2,
        "c": 3
    },
    "area2":{
        "d":4,
        "e":5,
        "f":6
    }
}
print(number["area1"]["a"])
print(number["area2"]["f"])