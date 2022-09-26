from collections import deque
from itertools import product

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
            return 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1:
                max_area = max(dfs(row, col), max_area)
        return max_area