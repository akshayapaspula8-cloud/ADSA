def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Find rows and columns containing zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set required rows to zero
    for i in zero_rows:
        for j in range(cols):
            matrix[i][j] = 0

    # Set required columns to zero
    for j in zero_cols:
        for i in range(rows):
            matrix[i][j] = 0

    return matrix