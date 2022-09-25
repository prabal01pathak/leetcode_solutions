from collections import deque
from itertools import product

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        def dfs(grid, i, j):
            if (
                i<0 or j<0 or
                i >= rows or j>=cols or
                grid[i][j] != "1"
            ):
                return
            grid[i][j] = "#"
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            
        island = 0
        for r, c in product(range(rows), range(cols)):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                island += 1
        return island
        
