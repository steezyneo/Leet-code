def guess(num): #API
    pass

def guessNumber(n: int) -> int:
    left = 0
    right = n

    while n>0:
        mid = left + (right - left)//2
        if guess(mid) == 0:
            return mid
        elif guess(mid) < 0:
            right = mid - 1
        else:
            left = mid + 1

    return left