def countBits(n: int) -> list[int]:           
    res = [0] * (n+1)
    for i in range(1,n+1):
        res[i] = res[i>>1] + (i & 1)
    return res            
print(countBits(5))


"""
c = []
for i in range(0,n+1):
    c.append(bin(i)[2:])
res = [0]   
c = c[1:]
for j in c:
    count = 0
    x = len(j)
    while(x!=0):
        if '1' in j:
            count += 1
            j = j[count:]
            if '1' not in j:
                res.append(count)
        x-=1
return res

"""