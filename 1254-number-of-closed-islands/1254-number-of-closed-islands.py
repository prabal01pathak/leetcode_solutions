from collections import deque
from itertools import product

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        self.hs = set()
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 0 and (row, col) not in self.hs:
                b = self.dfs(grid, row, col)
                res += 1 if b else 0
        return res

    def dfs(self, grid, i, j):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return False
        if grid[i][j] == 1:
            return True
        if (i, j) in self.hs:
            return True
        self.hs.add((i, j))
        top = self.dfs(grid, i-1, j)
        bottom = self.dfs(grid, i+1, j)
        left = self.dfs(grid, i, j-1)
        right = self.dfs(grid, i, j+1)
        return top and bottom and left and right 