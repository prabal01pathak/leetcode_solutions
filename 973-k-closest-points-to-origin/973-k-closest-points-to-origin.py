from collections import defaultdict
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = defaultdict(list)
        for point in points:
            e_d = sqrt(point[0]*point[0] + point[1]*point[1])
            h[e_d].append(point)
        key = list(h.keys())
        heapq.heapify(key)
        res = []
        done = 0
        for i in range(k):
            if done == k:
                break
            v = heapq.heappop(key)
            points = h[v]
            for point in points:
                done += 1
                res.append(point)
        return res[:k]
        