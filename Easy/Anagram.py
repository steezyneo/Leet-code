def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    charS = {}
    freq = 1
    for c in s:
        if c not in charS:
            charS[c] = freq
        elif c in charS:
            charS[c] += 1

    charT = {}
    freq = 1
    for c in t:
        if c not in charT:
            charT[c] = freq
        elif c in charT:
            charT[c] += 1
    return charS == charT

# Test cases
# isAnagram("abcc", "ccac")
print(isAnagram("aacc", "ccaa")) 

        