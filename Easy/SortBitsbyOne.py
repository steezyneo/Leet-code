def sortByBits(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda i: (bin(i).count('1'), i))

arr = [0,1,2,3,4,5]
sorted_arr = sortByBits(arr)

print(sorted_arr) 
