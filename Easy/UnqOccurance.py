from collections import Counter

def uniqueOccurrences(arr: list[int]):
    # dict = {}
    
    # for i in arr:
    #     if i in dict:
    #         dict[i] += 1
    #     else:
    #         dict[i] = 1

    # count =  list(dict.values()) 

    # return len(count) == len(list(set(count)))
    counter = Counter(arr)
    count = list(counter.keys())

    return len(count) == len(list(set(count)))



print(uniqueOccurrences([1,2]))