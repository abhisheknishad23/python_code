start = int(input('Enter start number= '))
stop = int(input('Enter stop number= '))

skip = int(input('Enter you wanna skip number = '))

for i in range(start, stop):
    if i ==skip:
        continue
    print(i)