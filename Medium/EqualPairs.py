from collections import Counter

def equalPairs(grid):
    rows = Counter(tuple(arr) for arr in grid)  #list can't be dictionary keys, so it's converted into a tuple
    count = 0

    for col in zip(*grid): #Transpose of a Matrix
        if col in rows:
            count += rows[col]

    return count    

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))