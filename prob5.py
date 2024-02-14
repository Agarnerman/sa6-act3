def power_list(nums, n):
    powered = list(map(lambda x: x ** n, nums))
    return powered

num_list = [2,13,1,12,41,12]
n = 2
result = power_list(num_list, n)
print("numbers raised by the power of",n, result)