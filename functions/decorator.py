def decorator(func):
    def wrapper():
        print('function before callled')
        func()
        print('function after called')
    return wrapper

@decorator
def hello():
    print('hello')
hello()