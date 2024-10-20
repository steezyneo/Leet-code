def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for ast  in asteroids:
        while stack and ast < 0 and stack[-1] > 0: 
            if abs(ast) > stack[-1]:
                stack.pop()  
                continue
            elif abs(ast) == stack[-1]:
                stack.pop()  
            break
        else:
            stack.append(ast)
    
    return stack


asteroids = [5,10,-5]
print(asteroidCollision(asteroids))

    