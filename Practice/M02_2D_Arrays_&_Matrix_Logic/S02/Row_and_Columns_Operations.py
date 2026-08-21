'''
#1351
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    count += 1
        return count
Input:
grid =[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output:
8

if rows are sorted 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = m - 1  
        col = 0      
        cou= 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)
                row -= 1  
            else:
                col += 1  
        return count

#832
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1 
                else:
                    row[i] = 0
        return image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                 row[i] = 1 - row[i]
        return image
'''