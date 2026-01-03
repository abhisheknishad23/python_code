#write a program to find the fibonacci series up to n.
#The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers. You can generate the sequence up to n terms. For example:
def fibonacci(n):
    fib_series = [0,1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1]+fib_series[-2])

    return fib_series[:n]