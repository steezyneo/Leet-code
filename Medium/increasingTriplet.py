def increasingTriplet(nums: list[int]):
    leftMin = [0]*len(nums)
    leftMin[0] = nums[0]
    for i in range(1, len(nums)):
        leftMin[i] = min(leftMin[i-1], nums[i])

    rightMax = [0]*len(nums)
    rightMax[len(nums)-1] = nums[len(nums)-1]
    rightMax[len(nums)-1] = nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        rightMax[i] = max(rightMax[i+1], nums[i])
    
    for i in range(len(nums)):
        if (leftMin[i] < nums[i] < rightMax[i]):
            return True
    return False

nums = [1,2,3,4,5]
print(increasingTriplet(nums))
    
