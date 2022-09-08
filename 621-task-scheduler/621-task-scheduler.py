from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        queue = deque()
        time = 0
        for t in tasks:
            count[ord(t) - ord("A")] -= 1
        count = [i for i in count if i!=0]
        print(count)
        heapq.heapify(count)
        while len(queue) > 0 or len(count) > 0:
            if len(queue) > 0 and queue[0][1] == time:
                heapq.heappush(count, queue.popleft()[0])
            time += 1
            value = 0
            if len(count) > 0:
                value = heapq.heappop(count)
            if not (value == 0 or 0 == value+1):
                queue.append([value+1,time+n])
        return time