from collections import deque
from itertools import product

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        island = 0
        
        def bfs(r, c):
            queue = deque([ (r, c) ])
            visited.add((r, c))
            while queue:
                x, y = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = x+ dr, y + dc
                    if (
                        (r in range(rows)) and
                        (c in range(cols)) and
                        grid[r][c] == '1' and
                        (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
                
        
        for r, c in product(range(rows), range(cols)):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                island += 1
        return island