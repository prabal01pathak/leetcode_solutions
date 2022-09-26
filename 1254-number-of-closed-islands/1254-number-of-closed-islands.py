from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.hs = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in self.hs:
                    b = self.dfs(grid, i, j)
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