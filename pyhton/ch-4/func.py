#write a function that prints hello world
# def hello():
#     print("hello world")

# hello() 

#function which takes 2 numbers as input and returns their sum
# def add(n1=0, n2=2):
#     print("n1:", n1)
#     print("n2:", n2)
#     sum = n1+n2
#     return sum

#position arguments
#print("The sum is", add(3,5))

#keyword arguments (named arguments)
#print("The sum is", add(n2=2, n1=3))

#default arguments
#print("The sum is", add())

#arbitary arguments
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

# output = addAllNumbers(1,2,3,4,5)
# print("The sum is ", output)

def student(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
student(name="don", age=23, city="yumlok")
student(name="thief", age=24, city="dhartilok")