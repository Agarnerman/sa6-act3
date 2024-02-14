def intersection(list1, list2):
    intersect = list(filter(lambda x: x in list2, list1))
    return intersect

list1 = [12,31,314,1,12,414]
list2 = [1,34,414,314,3111,4,16,13]
result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)