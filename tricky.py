#what is output and  why 
# def add_item(item, lst=[]):
#     lst.append(item)

# print(add_item(1))
# print(add_item(2))
# print(add_item(3,[]))
# print(add_item(4))

# def add_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst

# print(add_item(1))
# print(add_item(2))

# x = 10
# def func():
#     print(x)
#     x = 5

# func()

a = [1, 2, 3]
b = a[:]
a.append(4)
print(b)
