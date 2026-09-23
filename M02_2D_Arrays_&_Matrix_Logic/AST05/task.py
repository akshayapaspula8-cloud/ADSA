def diagonalBoundarySum(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        for j in range(n):
            # Boundary elements
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                total += arr[i][j]

            # Diagonal elements excluding boundary
            elif i == j or i + j == n - 1:
                total += arr[i][j]

    return total