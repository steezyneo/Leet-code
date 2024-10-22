def reverseWords(s: str):
    words = s.split(" ")
    words = [i for i in words if i!=""]
    words.reverse()
    return ' '.join(words)
    # s = s+' '
    # words = []
    # str = ""

    # i = 0
    # while i < len(s):
    #     if s[i] != " ":
    #         str += s[i]
    #         i+=1
    #     else:
    #         words.append(str+" ")
    #         str = ""
    #         i+=1

    # words = [i for i in words if i!=""]

    # words.reverse()
    
    # return ''.join(words)

s = "example   good a "
print(reverseWords(s))

