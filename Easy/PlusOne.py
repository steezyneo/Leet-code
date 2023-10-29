def plusOne(digits: list[int]) -> list[int]:
    d = 0
    for digit in digits:
        d = d*10+digit 
    d += 1    
    digits.clear()
    
    while d>0:
        last = d%10
        digits.insert(0, last)
        d //= 10

    return digits
print(plusOne([1]))