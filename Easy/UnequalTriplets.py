def unequalTriplets(nums: list[int]) -> int:
    l = len(nums)
    count = 0
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if (nums[i] != nums[j]) and (nums[i] != nums[k]) and (nums[j] != nums[k]):
                    count+=1

    return count

print(unequalTriplets([4,4,2,4,3]))
