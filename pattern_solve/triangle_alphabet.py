print("print equilateral tiangle pyramid with character")
size = 7
asciinum = 65
m=(2* size) - 2
for i in range(0, size):
    for j in range(0,m):
        print(end=" ")
    m = m-1
    for j in range(0, i+1):
        character = chr(asciinum)
        print(character, end=' ')
        asciinum +=1
    print(" ")