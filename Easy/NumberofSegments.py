def countSegments(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if (i == 0 or s[i - 1]==" ") and s[i]!=" ":
            count += 1
    return count

    # return len(s.split())

print(countSegments("love live! mu'sic forever"))