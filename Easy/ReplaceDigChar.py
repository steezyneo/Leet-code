def shift(c, x):
        return chr((ord(c) - ord('a') + x) % 26 + ord('a'))

def replaceDigits(s: str) -> str:
    nums = [x for x in s]
    for i in range(1, len(nums), 2):
        nums[i] = shift(nums[i-1], int(nums[i]))

    return "".join(nums)

print(replaceDigits("a1b1c1"))