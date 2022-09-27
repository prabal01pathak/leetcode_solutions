from collections import deque
from itertools import product

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()
        def dfs(r, c):
            if (
                r < 0 or r >= rows or c < 0 or c >= cols
                or grid2[r][c] == 0 or (r, c) in visited
               ):
                return True
            visited.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False
            res = dfs(r-1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c-1) and res 
            res = dfs(r, c+1) and res
            return res
        count = 0
        for row, col in product(range(rows), range(cols)):
            if grid2[row][col] == 1 and (row, col) not in visited and dfs(row, col):
                count += 1
        return count
                
                