def reverseVowels(s: str):
    strlist = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowStr = []
    for i in s:
        strlist.append(i)
        if i in vowels:
            vowStr.append(i)

    revVowStr = []
    for i in range(len(vowStr)-1, -1, -1):
        revVowStr.append(vowStr[i])
    
    j = 0
    for i in range(len(strlist)):
        if strlist[i] in vowels:
            strlist[i] = revVowStr[j]
            j+=1

    return ''.join(strlist)

print(reverseVowels("hello"))