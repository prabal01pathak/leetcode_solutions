from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        first = image[sr][sc]
        visited = set()
        queue = deque([ (sr, sc) ])
        count = 0
        while queue:
            print(queue)
            x, y = queue.popleft()
            if (x, y) in queue:
                continue
            visited.add((x, y))
            value = image[x][y]
            if first == value:
                image[x][y] = color
                if x != len(image) -1:
                    t = (x+1, y)
                    if not t in visited:
                        queue.append(t)
                if x != 0:
                    t = (x-1, y)
                    if not t in visited:
                        queue.append(t)
                if y != 0:
                    t = (x, y-1)
                    if not t in visited:
                        queue.append(t)
                if y != len(image[0])-1:
                    t = (x, y+1)
                    if not t in visited:
                        queue.append(t)
        return image