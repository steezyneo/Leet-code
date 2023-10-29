def pivotIndex(nums: list[int]) -> int:
    left = []
    right = []
    k = 0
    while k<len(nums):
        left = nums[ :k]
        right = nums[k+1: ]
        if sum(left) == sum(right):
            return k
        else:
            k+=1
    return -1

print(pivotIndex([1]))