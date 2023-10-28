def addDigits(num: int) -> int:
    if num < 10: return num
    total = 0
    while(len(str(num))!=1):
        digits = [int(d) for d in str(num)]
        total += sum(digits)
        num = total
        if(len(str(total))!=1):
            digits.clear()
            total = 0
    return total


print(addDigits(4))
