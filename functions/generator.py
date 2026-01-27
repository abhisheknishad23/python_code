#yield keyword

def count(num):
    while num > 0:
        yield num
        num -=1

#using the generator
for number in count(5):
    print(number)