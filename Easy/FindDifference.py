def findDifference(nums1: list[int], nums2: list[int]):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))

    unqNums1 = []
    unqNums2 = []
    for num in nums1:
        if num not in nums2:
            unqNums1.append(num)
    for num in nums2:
        if num not in nums1:
            unqNums2.append(num)
    
    return [unqNums1, unqNums2]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))

