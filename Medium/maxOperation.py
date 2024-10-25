def maxOperations(nums: list[int], k: int):
    opr = 0
    nums = sorted(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == k:
            opr += 1
            l += 1
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    return opr



nums = [3,1,3,4,3]
k = 6
print(maxOperations(nums, k))