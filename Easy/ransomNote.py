def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag = list(magazine)      
    ran = list(ransomNote)
    for i in ran:
        if i in mag:
            mag.remove(i)
        elif ran[i] not in mag:
            return False
    return True

print(canConstruct("aab", "baa"))

            