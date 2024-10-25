def maxArea(height: list[int]):
    max = 0
    l = 0
    r = len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        if area > max:
            max = area
        if min(height[l], height[r]) == height[l]:
            l += 1
        else:
            r -= 1
    return max

height = [1,1]
print(maxArea(height))