def maxVowels(s: str, k: int):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = cnt = 0
    l = 0
    for r in range(len(s)):
        if s[r] in vowels: cnt += 1     
        if r - l + 1 > k:
            if s[l] in vowels: cnt-= 1
            l += 1
        res = max(res, cnt)
    return res
    

s = "abciiidef" 
k = 3
print(maxVowels(s, k))