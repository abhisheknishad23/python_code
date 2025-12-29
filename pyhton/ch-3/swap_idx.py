#given a list in python and provided the index of the elements
#write a program to swap the two elements in the list
#input : list=[23,65,19,90]=0, idx2=2
#output: [19,65,23,90]

n= int(input("Enter size of list: "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index1: "))
idx2 = int(input("Enter index2: "))
print(list)

#swapping values at idx1 and idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)