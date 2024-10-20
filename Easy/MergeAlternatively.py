def mergeAlternately(word1: str, word2: str):
    merged = []

    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
        i+=1


    return ''.join(merged)   


word1 = "abcd"
word2 = "pqr"
print(mergeAlternately(word1, word2))