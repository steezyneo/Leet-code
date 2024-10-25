def moveZeroes(nums: list[int]):
    l = 0
    for r in range(len(nums)):
        if nums[r]!=0:
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp
            l += 1

    return nums
        # zeroCount = 0
        # arr = []
        # for i in nums:
        #     if i != 0:
        #         arr.append(i)
        #     else:
        #         zeroCount+=1

        # for i in range(zeroCount):
        #     arr.append(0)

        # nums = arr

        # return nums
        
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))