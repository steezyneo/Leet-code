def canPlaceFlowers(flowerbed: list[int], n: int):
    flowers = [0] + flowerbed + [0]
    for i in range(1, len(flowers)-1):
        if flowers[i-1] == 0 and flowers[i] == 0 and flowers[i+1] == 0:
            flowers[i] = 1
            n-= 1
    
    return n == 0


flowerbed = [1,0,0,0]
n = 1
print(canPlaceFlowers(flowerbed, n))