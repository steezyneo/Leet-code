def largestAltitude(gain: list[int]) -> int:
    newGain = [0] + gain
    currentGain = 0

    for i in range(len(gain)):
        currentGain = newGain[i] + gain[i]
        newGain[i+1] = currentGain
        
    return max(newGain)


gain = [-5,1,5,0,-7]
print(largestAltitude(gain))