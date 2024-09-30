def longestSquareStreak(nums: list[int]) -> int:
    if not nums:
        return -1  

    nums = sorted(nums) 
    longest_streak = 2  
    current_streak = 2  

    for i in range(2, len(nums)):
        if nums[i] == nums[i - 1] * nums[i - 1]:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 2

    return longest_streak if longest_streak >= 2 else -1
print(longestSquareStreak([5,12,3,10,4,11,4,16,11]))