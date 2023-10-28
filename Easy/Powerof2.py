def isPowerOfTwo(n: int) -> bool:
    if n <= 0: return False
    while (n & 1) != 1:
        n >>= 1
    return n==1 

print(isPowerOfTwo(16))

# while(n!=1):
    #     n /= 2
    # return n==1