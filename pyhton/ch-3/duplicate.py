#given three arrays we have to find common elements in three sorted lists using sets.
#input: ar1 = [1,5,10,30,40]
#ar2 = [2,40,34,5,30]
#ar3 = [3,4,55,40,54,30,50]
#output: [30, 40]

l1 = [1,5,10,30,40]
l2 = [3,4,5,24,10]
l3 = [5,3,5,10]

#type casting into sets
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

#join using intersection
s1s2  = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)