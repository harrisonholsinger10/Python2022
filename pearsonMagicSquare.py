def magicSquare(x):
    size = len(x[0])
    lst = []

    for i in range(size):
        lst.append(sum(r[i] for r in x))
        lst.extend([sum (lines) for lines in x])
    result = 0


    for i in range(0,size):
        result += x[i][i]

    lst.append(result)

    final_result = 0
    
    for i in range(size-1,-1,-1):
        final_result += x[i][i]
        
    lst.append(final_result)
    
    if len(set(lst))>1:
        return False
    return True

print(magicSquare([[4,9,2], [3,5,7], [8,1,6]]))
print(magicSquare([[2,7,6], [9,5,1], [4,3,8]]))
print(magicSquare([[1,2,3], [4,5,6], [7,8,9]]))
print(magicSquare([[4,9,2], [3,5,5], [8,1,6]]))
