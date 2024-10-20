from collections import Counter
from itertools import count

def closeStrings(word1: str, word2: str):
    if set(word1) != set(word2):
        return False
        
    return sorted(Counter(word1).values()) , sorted(Counter(word2).values())
            

    

word1 = "caaabb"
word2 = "aabbbc"
print(closeStrings(word1, word2))