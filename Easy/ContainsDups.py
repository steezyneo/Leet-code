def containsDuplicate(nums: list[int]) -> bool:
    org = set()
    for num in nums:
        org.add(num)
    if len(nums) != len(org):
        return True
    return False
        

print(containsDuplicate([5,5,6,7,8]))
