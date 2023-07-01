matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
tmp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def m():
    for a in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(tmp)):
                tmp[i][j] = matrix[j][i]
        return tmp
    return
print(matrix)
print(m())
