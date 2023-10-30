def checkStraightLine(coordinates: list[list[int]]) -> bool:
    if len(coordinates) <= 2:
        return True

    for i in range(0, len(coordinates) - 2):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        x3, y3 = coordinates[i+2]

        if (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1):
            return False

    return True

print(checkStraightLine([[0,0],[0,5],[5,5],[5,0]]))  