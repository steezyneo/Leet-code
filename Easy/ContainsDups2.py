def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    indices = {}
    for i, num in enumerate(nums):
        if num in indices and abs(indices[num] - i) < k:
            return True
        indices[num] = i
    return False

print(containsNearbyDuplicate([1,0,1,1], 2))

# for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if(nums[i] == nums[j]):
#                 if (abs(i-j)) == k :
#                     return True
#     return False