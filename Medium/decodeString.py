def decodeString(s):
    stack = []

    for c in s:
        if c != ']':
            stack.append(c)
        else:
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()
            mul = ""
            while stack and stack[-1].isdigit():
                mul = stack.popA) + mul
            stack.append(substr * int(mul))

    return ''.join(stack)

s = "3[a]2[bc]"
print(decodeString(s))