from collections import deque
from itertools import product

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[rows-1][cols-1]:
            return -1
        queue = deque([(0,0,0)])
        minimum = float("inf")
        visited = set()
        while queue:
            x, y, d = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x,y))
            if x == rows -1 and y == cols -1: 
                minimum = min(minimum, d)
            if x > 0 and grid[x-1][y] == 0:
                queue.append((x-1, y, d+1))
            if x < rows -1 and grid[x+1][y] == 0:
                queue.append((x+1, y, d+1))
            if y < cols -1 and grid[x][y+1] == 0:
                queue.append((x, y+1, d+1))
            if y > 0 and grid[x][y-1] == 0:
                queue.append((x, y -1, d+1))
            if x < rows -1 and y < cols -1 and grid[x+1][y+1]== 0:
                queue.append((x+1, y+1, d+1))
            if x > 0 and y > 0 and grid[x-1][y-1] == 0:
                queue.append((x-1, y -1, d+1))
            if x > 0 and y < cols -1 and grid[x-1][y+1] == 0:
                queue.append((x-1, y+1, d+1))
            if x < rows -1 and y > 0 and grid[x+1][y-1] == 0:
                queue.append((x+1, y -1, d+1))
        return minimum+1 if minimum != float("inf") else -1
            