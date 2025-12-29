#write a program to print numbers from n to 1.
#input
#n=5
#output:
# 5
# 4
# 3
# 2
# 1

def print_n_to_1(n):
    #base case
    if n==0:
        return
    
    print(n)
    #recursive case
    print_n_to_1(n-1)

print_n_to_1(5)