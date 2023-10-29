def addBinary(a: str, b: str) -> str:
    # num_a = int(a, 2)
    # num_b = int(b, 2)
    # sum = num_a + num_b
    # res = bin(sum)[2:]
    return str(bin(int(a, 2) + int(b, 2))[2:])
    
    

print(addBinary("11", "1"))