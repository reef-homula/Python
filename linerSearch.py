def LinerSearch(rangenum, snum):
    flag = "not found..."
    for i in rangenum:
        if i == snum:
            flag = "founded!"
            break
    return flag

nums = range(1, 101)
s1 = LinerSearch(nums, 3)
print(s1)
s2 = LinerSearch(nums, 99)
print(s2)
s3 = LinerSearch(nums, 108)
print(s3)