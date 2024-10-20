def removeStars(s: str) -> str:
    stack = []
    for char in s:
        if char!= "*":
            stack.append(char)
        else:
            stack.pop()
    s = "".join(stack)
    return s

            


print(removeStars("leet**cod*e"))
