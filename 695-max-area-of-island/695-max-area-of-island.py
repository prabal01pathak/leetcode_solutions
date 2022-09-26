from collections import deque
from itertools import product

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            if (r, c) in visited: return 0
            queue = deque([ (r, c) ])
            area = 0
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited: continue
                visited.add((x, y))
                if grid[x][y] == 1:
                    area += 1
                    if x > 0 : queue.append((x-1, y))
                    if x < rows -1: queue.append((x+1, y))
                    if y < cols-1: queue.append((x, y+1))
                    if y > 0: queue.append((x, y-1))
            return area
        max_area = 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1 and (row, col) not in visited:
                max_area = max(bfs(row, col), max_area)
        return max_area