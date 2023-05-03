nums = range(2, 30)
for i in range(2,10):
    nums = filter(lambda x: x == i or x % i, nums)
print(nums)