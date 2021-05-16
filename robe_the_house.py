def rob(nums):
    max_val = []

    max_val.append(nums[0])

    if nums[1] > nums[0]:
        max_val.append(nums[1])
    else:
        max_val.append(nums[0])
    
    if nums[0] + nums[2] > nums[1]:
        max_val.append(nums[0] + nums[2])
    else:
        max_val.append(nums[1])

    for i in range(3, len(nums)):
        a = max_val[i - 3] + nums[i]
        b = max_val[i - 2] + nums[i]

        max_val.append(a if a > b else b)

    x = max_val.pop()
    y = max_val.pop()
    return x if x > y else y

# print(rob([2, 70, 90, 50, 100, 200]))
print(rob([1, 2, 3, 1]))
