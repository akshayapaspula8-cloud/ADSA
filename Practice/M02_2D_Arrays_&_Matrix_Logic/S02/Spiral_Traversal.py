'''
#54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        res = []

        while top <= bottom and left <= right:
            # 1. Traverse Right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. Traverse Down
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. Traverse Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. Traverse Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res
'''