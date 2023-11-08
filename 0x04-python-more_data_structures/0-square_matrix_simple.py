def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    square_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * matrix[i][j])
        square_matrix.append(row)
    return square_matrix
