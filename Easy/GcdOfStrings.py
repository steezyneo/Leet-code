def gcdOfStrings(str1: str, str2: str):
    if str1 == str2:
        return str1
    
    if str1 < str2:
        str1, str2 = str2, str1

    if str1[:len(str2)] == str2:
        str1 = str1[len(str2):]
        return gcdOfStrings(str1, str2)
    
    return ""

str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1,str2))