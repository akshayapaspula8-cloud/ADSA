def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Sort diagonals starting from the first column
    for start_row in range(rows):
        diagonal = []
        i, j = start_row, 0

        while i < rows and j < cols:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = start_row, 0
        k = 0
        while i < rows and j < cols:
            mat[i][j] = diagonal[k]
            k += 1
            i += 1
            j += 1

    # Sort diagonals starting from the top row
    for start_col in range(1, cols):
        diagonal = []
        i, j = 0, start_col

        while i < rows and j < cols:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = 0, start_col
        k = 0
        while i < rows and j < cols:
            mat[i][j] = diagonal[k]
            k += 1
            i += 1
            j += 1

    return mat