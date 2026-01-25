#find tha largest element

arr = list(map(int, input("Enter array elements").split()))

max_val = arr[0]
for num in arr:
    if num> max_val:
        max_val = num

print("Largest element", max_val)