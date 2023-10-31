import math
def isPowerOfFour(n: int) -> bool:
    return n > 0 and math.log(n, 4) % 1 == 0

print(isPowerOfFour(16))
        