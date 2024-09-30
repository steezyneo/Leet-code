def findArray(pref: list[int]) -> list[int]:
    result = [pref[0]]
    for i in range(1, len(pref)):
        xor = pref[i-1] ^ pref[i] 
        result.append(xor)
     
    return result

pref = [5, 2, 0, 3, 1]
result = findArray(pref)
print(result)  

