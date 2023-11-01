def shuffle(nums: list[int], n: int) -> list[int]:
    y_arr = nums[n:]  
    nums = nums[:n]   
    k=1 
    i=0
    while i < len(y_arr):
        nums.insert(k, y_arr[i])
        k+=2
        i+=1
    return nums

print(shuffle([2,5,1,3,4,7], 3))