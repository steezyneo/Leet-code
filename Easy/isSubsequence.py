def isSubsequence(s: str, t: str):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    return i == len(s)

s = ""
t = "axysbkl"
print(isSubsequence(s,t))