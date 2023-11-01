def integerReplacement(n: int) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
            count+=1
        else:
            n=n+1
            count+=1
    return count

print(integerReplacement(6))