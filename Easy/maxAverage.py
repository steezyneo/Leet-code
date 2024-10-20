def findMaxAverage(nums: list[int], k: int) -> float:
    currentSum = sum(nums[:k])
    maxAvg = currentSum / k

    for i in range(k, len(nums)):
        currentSum += nums[i] - nums[i-k]
        maxAvg = max(maxAvg, currentSum/k)

    return maxAvg

nums = [5]
k = 1
print(findMaxAverage(nums, k))
