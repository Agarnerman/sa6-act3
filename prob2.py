list = ["apple", "banana", "kiwi", "antonio", "comp3081", "supercalafragalisticexpialidoious"]
sorted_list = sorted(list, key=lambda x: (len(x), x))

print(sorted_list)