def compress(chars: list[str]) -> int:
    if len(chars) < 2:
        return len(chars)

    count = 1
    arr = []
    i = 0
    j = 1

    while j < len(chars):
        if chars[j] == chars[i]:
            count += 1
        else:
            arr.append(chars[i])
            if count > 1:
                arr.extend(list(str(count)))
            i = j
            count = 1
        j += 1

    arr.append(chars[i])
    if count > 1:
        arr.extend(list(str(count)))

    for k in range(len(arr)):
        chars[k] = arr[k]

    return len(arr)


chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
