def find_max(nums, comp_lambda):
    if nums == ():
        return None
    max = nums[0]
    for num in nums[1:]:
        max = comp_lambda(max, num)
    return max

list = [1,2,3,4,5,212,31,43]
max_num = find_max(list, lambda x, y: x if x > y else y)
print("max number:", max_num)