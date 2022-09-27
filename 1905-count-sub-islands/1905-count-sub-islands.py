from collections import deque
from itertools import product

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()
        def bfs(r, c):
            queue = deque([ (r, c) ])
            is_valid = True
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if grid2[x][y] == 1:
                    if grid1[x][y] != 1:
                        is_valid = False
                    if x > 0: queue.append((x-1, y))
                    if y > 0: queue.append((x, y-1))
                    if x < rows -1: queue.append((x+1, y))
                    if y < cols -1: queue.append((x, y+1))
            return 1 if is_valid else 0
        res = 0
        for row, col in product(range(rows), range(cols)):
            if grid2[row][col] == 1 and (row, col) not in visited:
                res += bfs(row, col)
        return res
                
                