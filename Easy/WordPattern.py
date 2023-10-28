def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_dict = {}
    word_dict = {}

    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        if char not in pattern_dict and word not in word_dict:
            pattern_dict[char] = word
            word_dict[word] = char
        elif char in pattern_dict and word in word_dict:
            if pattern_dict[char] != word or word_dict[word] != char:
                return False
        else:
            return False
    
    return True


print(wordPattern("abba", "dog cat cat dog"))
