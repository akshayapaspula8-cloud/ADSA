''' 
#1572 
class Solution:

  def diagonalSum(self, mat: list[list[int]]) -> int:
    n = len(mat)
    total_sum = 0
    for i in range(n):
      for j in range(n):
        if i == j or i + j == n - 1:
          total_sum += mat[i][j]

    return total_sum

#498 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat), len(mat[0])
        res = []
        for d in range(rows + cols - 1):
            diagonal = []
            r = 0 if d < cols else d - cols + 1 
            c = d if d < cols else cols - 1
            while r < rows and c >= 0:
                diagonal.append(mat[r][c])
                r += 1 
                c -= 1
            if d % 2 == 0:
                diagonal.reverse()
            res += diagonal 
        return res       
    
#1380

'''