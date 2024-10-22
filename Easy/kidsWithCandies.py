def kidsWithCandies(candies: list[int], extraCandies: int):
    max = 0
    for i in candies:
        if i > max:
            max = i

    result = []
    for i in candies:
        if (i + extraCandies) >= max:
            result.append(True)
        else:
            result.append(False)

    return result

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))