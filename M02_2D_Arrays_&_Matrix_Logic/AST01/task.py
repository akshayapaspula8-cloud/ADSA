from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = [[rStart, cStart]]
    
    r, c = rStart, cStart
    step = 1
    
    while len(result) < rows * cols:
        # Right
        for _ in range(step):
            c += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        # Down
        for _ in range(step):
            r += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        step += 1
        
        # Left
        for _ in range(step):
            c -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        # Up
        for _ in range(step):
            r -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        
        step += 1
    
    return result


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))