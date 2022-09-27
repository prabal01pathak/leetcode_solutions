from collections import deque
from itertools import product

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited: set = set()
            
        def bfs(r: int, c: int) -> int:
            queue = deque([ (r, c) ])
            count = 0
            if_count = True
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if grid[x][y] == 1:
                    count += 1
                    print("X: ", x, "Y: ", y)
                    if (x == 0 or x == rows -1 or y == 0 or y == cols -1):
                        if_count = False
                    print("X: ", x, "Y: ", y)
                    if x > 0: queue.append((x-1, y))
                    if x < rows - 1: queue.append((x+1, y))
                    if y > 0: queue.append((x, y-1))
                    if y < cols - 1: queue.append((x, y+1))
            return count if if_count else 0
        
        res: int = 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1 and (row, col) not in visited:
                res += bfs(row, col)
                print("res: ", res, "xy: ", (row, col))
        return res